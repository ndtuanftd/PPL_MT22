"""
 * @author nhphung
"""
from AST import *
# Have to import Visitor because CodeGenerator does not import by itself
# What the fuck is this chain of responsibility?
from Visitor import *
from StaticError import *

# !!! COMMENT THIS OUT
from main.d96.utils.AST import *


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value


class MetaAttribute: # var in the class scope
    def __init__(
        self,
        name: str,
        type: Type,
        init: bool,
        static: bool = False,
        constant: bool = False
    ):
        self.name = name
        self.type = type
        self.init = init
        self.static = static
        self.constant = constant


class MetaVariable: # var in the method scope
    def __init__(
        self,
        name: str,
        type: Type,
        scope: int,
        init: bool,
        constant: bool = False
    ):
        self.name = name
        self.type = type
        self.scope = scope
        self.init = init
        self.constant = constant


class MetaMethod: # function
    def __init__(
        self,
        cls: str,
        name: str,
        partype: List[VarDecl],
        rettype: Type = None,
        static: bool = False
    ):
        if cls == 'Program' and name == 'main' and not partype:
            static = True
        partype_list = list(map(lambda x: x.variable.name, partype))
        partype_set = set(partype_list)
        if len(partype_list) != len(partype_set):
            raise Redeclared(Parameter(), name)

        self.name = name
        self.partype = partype
        self.rettype = rettype
        self.static = static

        # { str: List[MetaVariable] }
        # because we must keep track of variables in outer scope
        self.variable = {
            x.variable.name:
            [MetaVariable(x.variable.name, x.varType, 2, True, False)]
            for x in partype
        }

        # Not in loop
        self.loop = 0

        # Already in scope of class
        self.scope = 1

    def enter_loop(self):
        self.loop += 1

    def exit_loop(self):
        self.loop -= 1

    def enter_scope(self):
        self.scope += 1

    def exit_scope(self):
        self.scope -= 1
        # Remove inner scope variables
        for name, val in self.variable.items():
            if val and val[-1].scope > self.scope:
                self.variable[name].pop()

    def add_var(self, name: str, type: Type, init: bool):
        self.check_redeclared_variable(name)
        if name in self.variable.keys():
            self.variable[name] += [MetaVariable(name, type, self.scope, init)]
        else:
            self.variable[name] = [MetaVariable(name, type, self.scope, init)]

    def add_const(self, name: str, type: Type, init: bool):
        self.check_redeclared_const(name)
        if name in self.variable.keys():
            self.variable[name] += [
                MetaVariable(name, type, self.scope, True, init)
            ]
        else:
            self.variable[name] = [
                MetaVariable(name, type, self.scope, True, init)
            ]

    def get_or_raise_undeclared_variable(self, name: str):
        if name not in self.variable.keys():
            raise Undeclared(Variable(), name)
        return self.variable[name]

    def check_entrypoint(self):
        return self.name == 'main' and self.static

    def check_redeclared_variable(self, name: str):
        if name in self.variable.keys():
            variable = self.variable[name][-1]
            if self.scope <= variable.scope:
                raise Redeclared(Variable(), name)

    def check_redeclared_const(self, name: str):
        if name in self.variable.keys():
            const = self.variable[name][-1]
            if self.scope <= const.scope:
                raise Redeclared(Constant(), name)


# No MRO
# http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158569#p491360
# No forward reference
# http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158537#p491354
class MetaClass: # class
    # PEP 484: Forward reference
    def __init__(self, name: str, super_cls: 'MetaClass' = None):
        self.name = name
        self.attr = dict()
        self.method = dict()
        if super_cls:
            self.attr = super_cls.attr.copy()
            self.method = super_cls.method.copy()

    def add_attr(
        self,
        name: str,
        type: Type,
        init: bool,
        static: bool = False,
        constant: bool = False
    ):
        self.check_redeclared_attr(name)
        self.attr[name] = MetaAttribute(name, type, init, static, constant)

    def add_method(
        self,
        name: str,
        partype: List[VarDecl],
        rettype: Type = None,
        static: bool = False
    ):
        self.check_redeclared_method(name)
        if name == 'Destructor' and partype:
            raise TypeMismatchInStatement(SpecialMethod())
        self.method[name] = MetaMethod(
            self.name, name, partype, rettype, static
        )

    def get_or_raise_undeclared_attr(self, name: str):
        if name not in self.attr.keys():
            raise Undeclared(Attribute(), name)
        return self.attr[name]

    def get_or_raise_undeclared_method(self, name: str):
        if name not in self.method.keys():
            if name == 'Constructor':
                self.method[name] = MetaMethod(self.name, name, [], None, False)
            else:
                raise Undeclared(Method(), name)
        return self.method[name]

    def check_entrypoint(self):
        return any(
            [method.check_entrypoint()
             for method in self.method.values()] if self.method else [False]
        )

    def check_redeclared_attr(self, name: str):
        if name in self.attr.keys():
            raise Redeclared(Attribute(), name)

    def check_redeclared_method(self, name: str):
        if name in self.method.keys():
            raise Redeclared(Method(), name)


class MetaProgram:
    def __init__(self):
        self.cls = dict()

    def add_class(self, name: str, super_cls=None):
        self.check_redeclared_class(name)
        if super_cls:
            self.check_undeclared_class(super_cls)
        self.cls[name] = MetaClass(
            name, self.cls[super_cls] if super_cls else None
        )

    def add_method(
        self,
        cls: str,
        name: str,
        partype: List[VarDecl],
        rettype: Type = None,
        static: bool = False
    ): # add function
        self.check_undeclared_class(cls)
        self.cls[cls].add_method(name, partype, rettype, static)

    def add_attr(
        self,
        cls: str,
        name: str,
        type: Type,
        init: bool,
        static: bool = False,
        constant: bool = False
    ): # add variable
        self.check_undeclared_class(cls)
        self.cls[cls].add_attr(name, type, init, static, constant)

    def get_class(self, name: str):
        self.check_undeclared_class(name)
        return self.cls[name]

    def check_entrypoint(self):
        return any(
            [cls.check_entrypoint()
             for cls in self.cls.values()] if self.cls else [False]
        )

    def check_type(self, match: Type, new: Type):
        t_match = type(match)
        t_new = type(new)

        if t_match is ClassType and t_new is ClassType:
            self.check_undeclared_class(match.classname.name)
            self.check_undeclared_class(new.classname)
        if t_match is t_new:
            return True
        if t_match is FloatType and t_new is IntType:
            return True
        if t_match is ArrayType and t_new is ArrayType:
            return match.size == new.size and self.check_type(
                match.eleType, new.eleType
            )
        return False

    def check_redeclared_class(self, name: str):
        if name in self.cls.keys():
            raise Redeclared(Class(), name)

    def check_undeclared_class(self, name: str):
        if name not in self.cls.keys():
            raise Undeclared(Class(), name)


class StaticChecker:
    # c: Tuple[MetaClass, MetaProgram]

    COERCE_TYPE = {
        FloatType: [IntType, FloatType],
        BoolType: [BoolType],
        IntType: [IntType],
        StringType: [StringType],
        ArrayType: [ArrayType],
        ClassType: [ClassType],
        VoidType: [VoidType]
    }

    # Assume that these functions exist
    global_env = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    def __init__(self, ast):
        self.ast = ast

    # Copy from BaseVisitor because it doesn't do shit
    def visit(self, ast, param):
        return ast.accept(self, param)

    # Copy from Utils because BKeL does not have this file
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def check(self):
        return self.visit(self.ast, None)

    def visitProgram(self, ast, c=global_env):
        self.meta_program = MetaProgram()

        # Traverse all classes
        [self.visit(x, c) for x in ast.decl]

        if not self.meta_program.check_entrypoint():
            raise NoEntryPoint()

        # All testcases are error-guaranteed
        # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158488#p491231

    def visitClassDecl(self, ast, c=None):
        # Load classes into meta_program
        self.meta_program.add_class(
            ast.classname.name, ast.parentname.name if ast.parentname else None
        )

        # Make classes load attributes and methods
        [
            self.visit(x, self.meta_program.get_class(ast.classname.name))
            for x in ast.memlist
        ]

    def visitAttributeDecl(self, ast, c: MetaClass):
        static = type(ast.kind) is Static
        const = type(ast.decl) is ConstDecl
        if const:
            partype = ast.decl.constType
            name = ast.decl.constant.name
            if not ast.decl.value:
                raise IllegalConstantExpression(ast)
            inittype = self.visit(ast.decl.value, c)
        else:
            partype = ast.decl.varType
            name = ast.decl.variable.name
            inittype = self.visit(
                ast.decl.varInit, c
            ) if ast.decl.varInit else None

        if inittype and not self.meta_program.check_type(partype, inittype):
            raise TypeMismatchInStatement(ast.decl)
        c.add_attr(name, partype, True if inittype else False, static, const)

    def visitMethodDecl(self, ast, meta_cls: MetaClass):
        static = type(ast.kind) is Static
        meta_cls.add_method(ast.name.name, ast.param, None, static)
        [
            self.visit(
                ast.body, (
                    meta_cls,
                    meta_cls.get_or_raise_undeclared_method(ast.name.name)
                )
            )
        ]

    def visitBlock(self, ast, c: tuple):
        meta_class, meta_method = c
        meta_method.enter_scope()
        [self.visit(x, c) for x in ast.inst]
        meta_method.exit_scope()

    def visitVarDecl(self, ast, c: tuple):
        meta_class, meta_method = c
        # Var can exist without being initialized
        if ast.varInit:
            ret = self.visit(ast.varInit, c)
            partype = type(ast.varType)
            rettype = type(ret)
            if partype is ClassType:
                self.meta_program.get_class(ast.varType.classname.name)
            if ret and rettype not in self.COERCE_TYPE[partype]:
                raise TypeMismatchInStatement(ast)
            if rettype is ArrayType:
                if not (
                    ret.eleType is type(ast.varType.eleType) and
                    ret.size == ast.varType.size
                ):
                    raise TypeMismatchInStatement(ast)

        if ast.varInit and type(ast.varInit) is not NullLiteral:
            if type(ast.varType) is ClassType and rettype is None:
                meta_method.add_var(ast.variable.name, ast.varType, False)
            else:
                meta_method.add_var(ast.variable.name, ast.varType, True)
        else:
            meta_method.add_var(ast.variable.name, ast.varType, False)

    def visitConstDecl(self, ast, c: tuple):
        meta_class, meta_method = c
        if not ast.value:
            raise IllegalConstantExpression(ast.value)
        ret = self.visit(ast.value, c)
        partype = type(ast.constType)
        rettype = type(ret)
        if partype is ClassType:
            self.meta_program.get_class(ast.constType.classname.name)
        if rettype not in self.COERCE_TYPE[partype]:
            raise TypeMismatchInConstant(ast)
        meta_method.add_const(ast.constant.name, ast.constType, True)

    def visitAssign(self, ast, c):
        meta_class, meta_method = c
        lhs = self.visit(ast.lhs, c)
        rhs = self.visit(ast.exp, c)

        if not lhs:
            raise Undeclared(Identifier(), ast.lhs.name)
        if type(ast.lhs) is FieldAccess:
            if type(ast.lhs.obj) is SelfLiteral:
                cls = meta_class
            else:
                obj = meta_method.get_or_raise_undeclared_variable(
                    ast.lhs.obj.name
                )[-1]
                cls = self.meta_program.get_class(obj.type.classname.name)
            cls.get_or_raise_undeclared_attr(ast.lhs.fieldname.name)
            partype = type(lhs)
        else:
            if type(ast.lhs) is not ArrayCell:
                lhs = lhs[-1]
            if type(lhs) is MetaVariable and lhs.constant:
                raise CannotAssignToConstant(ast)
            if type(lhs) is ArrayType:
                obj = meta_method.get_or_raise_undeclared_variable(
                    ast.lhs.arr.name
                )[-1]
                if obj.constant:
                    raise CannotAssignToConstant(ast)
            if type(ast.lhs) is ArrayCell:
                partype = type(lhs)
            else:
                partype = type(lhs.type)

        # Dirty
        if type(rhs) is list:
            rhs = rhs[-1]
            rettype = type(rhs.type)
        else:
            rettype = type(rhs)
        if rettype not in self.COERCE_TYPE[partype]:
            raise TypeMismatchInStatement(ast)

    # LHS of Assign
    def visitId(self, ast, c: tuple):
        meta_class, meta_method = c
        if ast.name not in meta_method.variable.keys():
            raise Undeclared(Identifier(), ast.name)
        return meta_method.variable[ast.name]

    def visitCallStmt(self, ast, c: tuple):
        meta_class, meta_method = c
        obj = self.visit(ast.obj, c)
        if type(ast.obj) is SelfLiteral:
            # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158559#p491356
            if meta_method.static:
                raise IllegalMemberAccess(ast)
            cls = meta_class
        else:
            obj = meta_method.get_or_raise_undeclared_variable(ast.obj.name)[-1]
            cls = self.meta_program.get_class(obj.type.classname.name)
        method = cls.get_or_raise_undeclared_method(ast.method.name)
        partype = [self.visit(x, c) for x in ast.param]

        # We don't care about rettype of statements
        # Else it would be expressions
        for x, y in zip(method.partype, partype):
            if type(y) not in self.COERCE_TYPE[type(x.varType)]:
                raise TypeMismatchInStatement(ast)

    def visitCallExpr(self, ast, c: tuple):
        meta_class, meta_method = c
        if ast.method.name[0] == '$':
            cls = self.meta_program.get_class(ast.obj.name)
        else:
            obj = self.visit(ast.obj, c)
            if type(obj) is ClassType:
                cls = self.meta_program.get_class(obj.classname.name)
            else:
                obj = obj[-1]
                cls = self.meta_program.get_class(obj.type.classname.name)
        method = cls.get_or_raise_undeclared_method(ast.method.name)
        partype = [self.visit(x, c) for x in ast.param]

        # Expression must return type
        if not method.rettype or len(method.partype) != len(partype):
            raise TypeMismatchInExpression(ast)
        for x, y in zip(method.partype, partype):
            if type(y) not in self.COERCE_TYPE[type(x.varType)]:
                raise TypeMismatchInExpression(ast)

        return method.rettype

    def visitIf(self, ast, c: tuple):
        meta_class, meta_method = c
        condition = self.visit(ast.expr, c)
        if type(condition) != BoolType:
            raise TypeMismatchInStatement(ast)

        if isinstance(ast.thenStmt, (Return, Block, If)):
            self.visit(ast.thenStmt, c)
        else:
            if isinstance(ast.thenStmt, (For, Break, Continue)):
                self.visit(ast.thenStmt, c)
            else:
                self.visit(ast.thenStmt, meta_class)

        if ast.elseStmt:
            if isinstance(ast.elseStmt, (Return, Block, If)):
                self.visit(ast.elseStmt, c)
            else:
                if isinstance(ast.elseStmt, (For, Break, Continue)):
                    self.visit(ast.elseStmt, c)
                else:
                    self.visit(ast.elseStmt, meta_class)

    def visitFor(self, ast, c):
        meta_class, meta_method = c
        meta_method.enter_scope()
        meta_method.enter_loop()

        # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158527#p491282
        counter = meta_method.get_or_raise_undeclared_variable(ast.id.name)[0]
        if counter.constant:
            # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158471#p491277
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        expr1 = self.visit(ast.expr1, c)
        if type(expr1) is not IntType:
            raise TypeMismatchInStatement(ast)
        expr2 = self.visit(ast.expr2, c)
        if type(expr2) is not IntType:
            raise TypeMismatchInStatement(ast)
        if ast.expr3:
            expr3 = self.visit(ast.expr3, c)
            if type(expr3) is not IntType:
                raise TypeMismatchInStatement(ast)

        self.visit(ast.loop, c)

        meta_method.exit_loop()
        meta_method.exit_scope()

    def visitBreak(self, ast, c):
        meta_class, meta_method = c
        if meta_method.loop < 1:
            raise MustInLoop(Break())

    def visitContinue(self, ast, c):
        meta_class, meta_method = c
        if meta_method.loop < 1:
            raise MustInLoop(Continue())

    def visitReturn(self, ast, c):
        meta_class, meta_method = c
        if meta_method.name == 'main' and meta_method.static and ast.expr:
            # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158535#p491233
            raise TypeMismatchInStatement(ast)
        meta_method.rettype = self.visit(ast.expr, c)

    def visitNewExpr(self, ast, c: tuple):
        cls = self.meta_program.get_class(ast.classname.name)
        cons = cls.get_or_raise_undeclared_method('Constructor')
        partype = [self.visit(x, c) for x in ast.param]
        constype = list(map(lambda x: x.varType, cons.partype))

        # Assuming one constructor per class
        if len(cons.partype) != len(partype):
            raise TypeMismatchInExpression(ast)

        for match, new in zip(constype, partype):
            if not self.meta_program.check_type(match, new):
                raise TypeMismatchInExpression(ast)
        return ClassType(cls.name)

    def visitFieldAccess(self, ast, c: tuple):
        meta_class, meta_method = c
        obj = self.visit(ast.obj, c)
        if type(obj) is ClassType:
            cls = meta_class
        else:
            obj = obj[-1]
            if not obj.init:
                raise Undeclared(Identifier(), ast.obj.name)
            obj_type = obj.type
            if type(obj_type) is ClassType:
                cls = self.meta_program.get_class(obj_type.classname.name)
            else:
                cls = self.meta_program.get_class(obj.name)
        attr = cls.get_or_raise_undeclared_attr(ast.fieldname.name)
        return attr.type

    def visitBinaryOp(self, ast, c: BinaryOp):
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)
        if type(left) is list:
            left = left[-1]
            left_type = type(left.type)
        else:
            left_type = type(left)
        if type(right) is list:
            right = right[-1]
            right_type = type(right.type)
        else:
            right_type = type(right)
        op = ast.op

        # Arithmetic
        if op == '%':
            if not (left_type is IntType and right_type is IntType):
                raise TypeMismatchInExpression(ast)
        if op in ['+', '-', '*', '/']:
            if not (
                left_type in [IntType, FloatType] and
                right_type in [IntType, FloatType]
            ):
                raise TypeMismatchInExpression(ast)
            if left_type is IntType and right_type is IntType:
                return IntType()
            return FloatType()

        # Boolean
        if op == '==.':
            if not (left_type is StringType and right_type is StringType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op in ['&&', '||']:
            if not (left_type is BoolType and right_type is BoolType):
                raise TypeMismatchInExpression(ast)
            return BoolType()

        # String
        if op == '+.':
            if not (left_type is StringType and right_type is StringType):
                raise TypeMismatchInExpression(ast)
            return StringType()

        # Relational
        if op in ['==', '!=']:
            # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158243#p490396
            if not (
                left_type is right_type and left_type in [IntType, BoolType]
            ):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if op in ['<', '>', '<=', '>=']:
            if not (
                left_type in [IntType, FloatType] and
                right_type in [IntType, FloatType]
            ):
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitUnaryOp(self, ast, c: UnaryOp):
        body = self.visit(ast.body, c)
        op = ast.op

        # Arithmetic
        if op == '-':
            if type(body) not in [IntType, FloatType]:
                raise TypeMismatchInExpression(ast)
            return IntType() if type(body) is IntType else FloatType()

        # Boolean
        if op == '!':
            if type(body) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitArrayLiteral(self, ast, c: tuple):
        partype = [self.visit(x, c) for x in ast.value]
        # http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=158504#p491368
        if len(partype) < 1:
            return NullLiteral()
        partype_set = set(map(lambda x: type(x), partype))
        if len(partype_set) > 1:
            raise IllegalArrayLiteral(ast)
        return ArrayType(len(partype), partype_set.pop())

    def visitArrayCell(self, ast, c: tuple):
        meta_class, meta_method = c
        arr = self.visit(ast.arr, c)[0]
        if type(arr.type) is not ArrayType:
            raise TypeMismatchInExpression(ast)

        # Index syntax: [1][1]
        idx_type = [self.visit(x, c) for x in ast.idx]

        for idx in idx_type:
            if type(idx) is not IntType:
                raise TypeMismatchInExpression(ast)

        obj = meta_method.get_or_raise_undeclared_variable(ast.arr.name)[-1]
        idx_size = list(map(lambda x: x.value, ast.idx))
        obj_size = list()
        _obj = obj.type
        while True:
            if type(_obj) is not ArrayType:
                break
            obj_size += [_obj.size]
            _obj = _obj.eleType
        for x, y in zip(idx_size, obj_size):
            if x < 0 or x >= y:
                raise TypeMismatchInExpression(ast)

        return arr.type.eleType

    def visitStringLiteral(self, ast, c):
        return StringType()

    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitSelfLiteral(self, ast, c):
        return ClassType(Id(c[0].name))

    def visitNullLiteral(self, ast, c):
        return None
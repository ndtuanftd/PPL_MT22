from Visitor import Visitor
from AST import *
from StaticError import *
from Utils import Utils
from functools import reduce

"""
    @param self:
    @param partype: type of parameters or 
    @param rettype: function return type or variable type
    @return:
"""

class ParamType:
    def __init__(self, name: str, typ: Type, inherit: bool or None, out: bool or None):
        self.name = name
        self.typ = typ
        self.inherit = inherit
        self.out = out

class MType:
    def __init__(self, partype: List[ParamType], rettype: Type or None = None):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name: str, mtype, value=None, kind=Function(), additiondict: dict = {}):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        # self.dimens = dimens
        self.additiondict = additiondict

class SymbolTable:
    def __init__(self):
        self.table = [{}]
        self.inLoop = 0
        self.param_table= {}
        self.isFirstReturnStmt = True

    def addSymbol(self, name: str, symbol: Symbol):
        #   check redeclare
        self.table[0][name] = symbol
    def addParSymbol(self, name: str, symbol: Symbol):
        #   check redeclare
        self.param_table[name] = symbol
    def findSymbol(self, name: str, kind: Kind, getFunc = lambda x: x, ast = None, isStmt = False, isFuncDecl = False):
        for scope in self.table:
            if name in scope.keys():
                if not TypeChecker.isTheSameType(scope[name].kind, kind):
                    if isFuncDecl:
                        raise Redeclared(kind, name)
                    if isStmt:
                        raise TypeMismatchInStatement(ast)
                    else:
                        raise TypeMismatchInExpression(ast)

                return getFunc(scope)

        return None

    def mergeParamTable(self):
        self.table[0].update(self.param_table)
        self.param_table = {}
    def enterLoop(self):
        self.inLoop += 1

    def exitLoop(self):
        self.inLoop -= 1

    def enterScope(self):
        self.table = [{}] + self.table

    def exitScope(self): # remove head
        self.table = self.table[1:]

    def nScope(self):
        return len(self.table)

    def checkEntryPoint(self) -> bool:
        for key, value in self.table[-1].items():
            if key == 'main' and TypeChecker.isFunc(value.kind) and TypeChecker.isVoid(value.mtype.rettype) and len(value.mtype.partype) == 0:
                return True
        return False

    def checkRedeclare(self, name: str, kind: Kind) -> bool:
        if self.nScope() > 1:
            if name in self.table[0].keys(): # check redeclare at current scope
                raise Redeclared(kind, name)
        else: # in global scope
            if name in self.table[-1].keys(): # if var is declared as function
                if (TypeChecker.isFunc(self.table[0][name].kind) and self.table[0][name].additiondict['ndeclTime'] > 0) \
                        or TypeChecker.isVariable(self.table[0][name].kind):
                    raise Redeclared(kind, name)


    def inferType(self, name: str, typ: Type, isFunc: bool):
        scope = self.findSymbol(name, Variable() if not isFunc else Function())
        if scope is None:
            raise Undeclared(Identifier() if not isFunc else Function(), name)
        else:
            if isFunc:
                scope[name].mtype.rettype = typ
            else:
                scope[name].mtype = typ

    def inferTypeOfParamFunc(self, fn_name, param_name, typ: Type):
        scope = self.findSymbol(fn_name, Function())
        if scope is None:
            raise Undeclared(Function(), fn_name)
        else:
            for param in scope[fn_name].mtype.partype:
                if param.name == param_name:
                    param.typ = typ
                    break


class TypeChecker:
    def __init__(self):
        pass

    @staticmethod
    def isBoolType(x):
        return type(x) == BooleanType

    def isInListOfType(x, lst):
        return type(x) in lst

    @staticmethod
    def isIntType(x):
        return type(x) == IntegerType

    def isIntLit(x):
        return type(x) == IntegerLit

    @staticmethod
    def isFloatType(x):
        return type(x) == FloatType

    def isAuto(x):
        return type(x) == AutoType

    def isVoid(x):
        return type(x) == VoidType

    def isArrayType(x):
        return type(x) == ArrayType

    def isArrayCell(x):
        return type(x) == ArrayCell

    def isId(x ):
        return type(x) == Id

    def isStringType(x):
        return type(x) == StringType
    @staticmethod
    def isNone(x):
        return type(x) == type(None)

    def isFunc(x):
        return type(x) == Function

    def isFuncDecl(x):
        return type(x) == FuncDecl

    def isFuncCall(x):
        return type(x) == FuncCall

    def isVariable(x):
        return type(x) == Variable

    def isCallStmt(x):
        return type(x) == CallStmt

    @staticmethod
    def isTheSameType(x, y):
        if (TypeChecker.isArrayType(x) and TypeChecker.isArrayType(y)):
            if len(x.dimensions) != len(y.dimensions):
                return False
            else:
                return reduce(lambda a, b: a and b, map(lambda c, d: c == d, x.dimensions, y.dimensions), True) and (type(x.typ) is type(y.typ))
        else:
            return (type(x) is type(y)) or (TypeChecker.isFloatType(x) and TypeChecker.isIntType(y))

    def arrayCellDimensCheck(indexlist: List[Expr], dimens, isFullIntLit: bool = False):
        if (len(indexlist) > len(dimens)):
            raise TypeMismatchInExpression(indexlist[len(dimens)])
        elif (len(indexlist) < len(dimens)):
            # else:
            if isFullIntLit:
                if reduce(lambda acc, ele: acc and ele, map(lambda x, y: x.val < y, indexlist, dimens[:len(indexlist)]), True):
                    return dimens[len(indexlist):]  # return extracted dimens
                else:
                    return False
            else:
                return dimens[len(indexlist):]  # return extracted dimens
        else:
            if isFullIntLit:
                return reduce(lambda a, b: a and b, map(lambda x, y: x.val < y, indexlist, dimens), True)
            else:
                return True

    @staticmethod
    def checkParamRedeclare(lst):
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i].name == lst[j].name:
                    raise Redeclared(Parameter(), lst[i].name)


class StaticChecker(Visitor):
    global_envi = [
        Symbol("readInteger", MType([], IntegerType())),
        Symbol("printInteger", MType([IntegerType()], VoidType())),
        Symbol("readFloat", MType([], FloatType())),
        Symbol("writeFloat", MType([FloatType()], VoidType())),
        Symbol("readBoolean", MType([], BooleanType())),
        Symbol("printBoolean", MType([BooleanType()], VoidType())),
        Symbol("readString", MType([], StringType())),
        Symbol("printString", MType([StringType()], VoidType())),
    ]

    def __init__(self, ast):
        self.ast = ast
        self.symbolTable = SymbolTable()
        self.isFirstReturnStmt = True

    def isFunScope(self):
        return len(self.symbolTable.table) == 2

    def isGlobalScope(self):
        return len(self.symbolTable.table) == 1

    def isInsideStmtScope(self):
        return len(self.symbolTable.table) > 2

    def isFirstReturn(self):
        return self.isFirstReturnStmt

    def visitReturnFirstTime(self):
        self.isFirstReturnStmt = False

    def resetFirstReturn(self):
        self.isFirstReturnStmt = True

    def visit(self, ast, param):
        return ast.accept(self, param)
    def check(self):
        return self.visit(self.ast, None)
    def lookup(self, name, lst, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def parsArgsSuperMatchingCheck(self, super_args: List[Expr], parentFn_params: List[ParamType], fn_decl_name):
        lesser_len = None
        if len(super_args) == 0 and len(parentFn_params) == 0:
            return True
        if len(super_args) < len(parentFn_params):
            lesser_len = len(super_args)
        else:
            lesser_len = len(parentFn_params)

        for i in range(lesser_len):
            super_arg = self.visit(super_args[i], None)
            if TypeChecker.isFuncCall(super_args[i]):
                fn_name = super_args[i].name
                if TypeChecker.isAuto(super_arg):
                    self.symbolTable.inferType(fn_name, parentFn_params[i].typ, True)
                    super_arg = parentFn_params[i].typ

            if TypeChecker.isAuto(parentFn_params[i].typ):
                self.symbolTable.inferTypeOfParamFunc(fn_decl_name, parentFn_params[i].name, super_arg)
                parentFn_params[i].typ = super_arg


            if not TypeChecker.isTheSameType(parentFn_params[i].typ, super_arg):
                raise TypeMismatchInExpression(super_args[i])

        if len(super_args) < len(parentFn_params):
            raise TypeMismatchInExpression(None) # TODO: fix
        elif len(super_args) > len(parentFn_params):
            raise TypeMismatchInExpression(super_args[lesser_len])
        else:
            return True


    def parsArgsSpecialFunMatchingCheck(self, args: List[Expr], params: List[Type]):
        lesser_len = None
        if len(args) < len(params):
            return False
        elif len(args) > len(params):
            return False
        elif len(args) > 1 or len(params) > 1:
            return False
        elif len(args) == 0 and len(params) == 0:
            return True
        else:
            if TypeChecker.isTheSameType(params[0], self.visit(args[0], None)):
                return True
            else:
                return False





    def parsArgsMatchingCheck(self, args: List[Expr], params: List[ParamType], fn_decl_name):
        lesser_len = None
        if len(args) < len(params):
            return False
        elif len(args) > len(params):
            return False
        else:
            for i in range(len(args)):
                arg_type = self.visit(args[i], None)
                if TypeChecker.isFuncCall(args[i]):
                    fn_name = args[i].name

                    if TypeChecker.isAuto(arg_type):
                        self.symbolTable.inferType(fn_name, params[i].typ, True)
                        arg_type = params[i].typ

                if TypeChecker.isAuto(params[i].typ):
                    # infer in the funcdecl
                    self.symbolTable.inferTypeOfParamFunc(fn_decl_name, params[i].name, arg_type)
                    params[i].typ = arg_type


                if not TypeChecker.isTheSameType(params[i].typ,arg_type):
                    return False
            # end for
            return True

    def visitProgram(self, ast: Program, param=global_envi):  # decls: List[Decl]
        # get all function declaration as prototype in global scope that allow function call before declaration
        for decl in ast.decls:
            if TypeChecker.isFuncDecl(decl):
                # add funcdecl to symbol table
                if self.symbolTable.findSymbol(decl.name, Function()) is None:
                    self.symbolTable.addSymbol(decl.name, Symbol(decl.name, MType([self.visit(para, param) for para in decl.params], decl.return_type),kind=Function(), additiondict={"inherit": decl.inherit, "ndeclTime": 0}))

        for decl in ast.decls:
            # decl.accept(self, param)
            self.visit(decl, param)
        if not self.symbolTable.checkEntryPoint():
            raise NoEntryPoint()


    # Decl ##################################################
    def visitVarDecl(self, ast: VarDecl, param):  # name: str, typ: Type, init: Expr
        """ # Invalid(Variable(), <variable-name>):
            - When a variable is declared in type auto without the initialization
        """
        name = ast.name
        typ = self.visit(ast.typ, param)

        self.symbolTable.checkRedeclare(name, Variable())
        self.symbolTable.addSymbol(name, symbol=Symbol(name, typ, kind=Variable()))

        rhs = None
        # check redeclare

        dimens = None

        if ast.init:
            rhs = self.visit(ast.init, typ) # visit init to get tye type
            if TypeChecker.isArrayType(typ):
                dimens = typ.dimensions

            if TypeChecker.isAuto(typ):
                typ = rhs  # lhs type = rhs type
            elif TypeChecker.isAuto(rhs):
                rhs = typ
                self.symbolTable.inferType(ast.init.name, typ, TypeChecker.isFuncCall(ast.init))

            if (not TypeChecker.isTheSameType(typ, rhs)) or (TypeChecker.isIntType(typ) and TypeChecker.isFloatType(rhs)):
                raise TypeMismatchInVarDecl(ast)
            else:
                self.symbolTable.inferType(name, typ, False)
        elif TypeChecker.isAuto(typ): # auto but does not have init
            raise Invalid(Variable(), name)
        else:  # not init
            if TypeChecker.isArrayType(typ):
                # dimens = typ.dimensions
                # typ = typ.typ
                typ = ast.typ
            self.symbolTable.inferType(name, typ, False)

    def visitFuncDecl(self, ast: FuncDecl, param):  # self, name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
        """
            # Redeclared(Function(): kind, <function-name>: str)
            - The declaration must be unique in its scope

            # InvalidStatementInFunction(<function-name>: str)
            - First statement in function with inherit parameter (rules in 2.3)
        """
        name = ast.name
        fun_prototype = self.symbolTable.findSymbol(name, Function(), lambda x: x, isFuncDecl = True)

        if fun_prototype[name].additiondict["ndeclTime"] == 0:
            fun_prototype[name].additiondict["ndeclTime"] += 1
        else:
            raise Redeclared(Function(), name)

        # visit params
        retTyp = self.visit(ast.return_type, param)
        paramTypeList = []
        paramNameList = []
        inheritFunName = ast.inherit
        inheritParamList = []
        firstStmt = ast.body.body[0] if len(ast.body.body) > 0 else None

        # process inherit
        if inheritFunName:
            inheritFunScope = self.symbolTable.findSymbol(inheritFunName, Function(), lambda x: x)
            if inheritFunScope is None:
                raise Undeclared(Function(), inheritFunName)
            else:
                # get inherit param
                inheritParamList = [param for param in inheritFunScope[inheritFunName].mtype.partype if param.inherit == True] # list[ParamType]
                inheritParamNameList = [param.name for param in inheritParamList]


                # check param
                for fn_param in self.symbolTable.table[-1][ast.name].mtype.partype:
                    if fn_param.name in paramNameList:
                        raise Redeclared(Parameter(), fn_param.name)
                    else:
                        paramNameList.append(fn_param.name)
                        paramTypeList.append(fn_param)
                # add function symbol
                mtype = MType(paramTypeList, retTyp)

        else:
            for fn_param in self.symbolTable.table[-1][ast.name].mtype.partype:
                if fn_param.name in paramNameList:
                    raise Redeclared(Parameter(), fn_param.name)
                else:
                    paramNameList.append(fn_param.name)
                    paramTypeList.append(fn_param)

        # open scope
        self.symbolTable.enterScope()

        # add parameter to scope
        for param in paramTypeList:
            self.symbolTable.addSymbol(param.name, symbol=Symbol(param.name, param.typ, kind=Variable(), additiondict={"inherit": param.inherit, "out": param.out}))

        if inheritFunName:
            if firstStmt is None:
                if len(inheritFunScope[inheritFunName].mtype.partype) > 0:
                    raise TypeMismatchInExpression(None)
            if TypeChecker.isCallStmt(firstStmt):
                # for super
                # add inherit   param to current scope
                if firstStmt.name != "preventDefault" and firstStmt.name != "super":
                    if len(inheritFunScope[inheritFunName].mtype.partype) >  0:
                        raise TypeMismatchInExpression(None)
                elif firstStmt.name == "super":
                    if not self.parsArgsSuperMatchingCheck(firstStmt.args, inheritFunScope[inheritFunName].mtype.partype, ast.name):
                        raise InvalidStatementInFunction(name)
                    else:
                        TypeChecker.checkParamRedeclare(inheritParamList)
                        # add inherit param to current scope
                        for fn_param in self.symbolTable.table[-1][ast.name].mtype.partype:
                            if fn_param.name in inheritParamNameList:
                                raise Invalid(Parameter(), fn_param.name)
                        # add inherit params from parent function
                        for param in inheritParamList:
                            self.symbolTable.addSymbol(param.name, symbol=Symbol(param.name, param.typ, kind=Variable(),
                                                                                 additiondict={"inherit": param.inherit,
                                                                                               "out": param.out}))
                elif firstStmt.name == "preventDefault" and len(firstStmt.args) != 0:
                    raise TypeMismatchInExpression(firstStmt.args[0])

            else:
                if len(inheritFunScope[inheritFunName].mtype.partype) > 0:
                    raise TypeMismatchInExpression(None)

        else:

            if type(firstStmt) is CallStmt and \
                    (firstStmt.name == "super" \
                     or firstStmt.name == "preventDefault" and len(firstStmt.args) == 0):
                raise InvalidStatementInFunction(name)

        fnBodyList = self.visit(ast.body, (ast.name, True))

        self.resetFirstReturn()





    def visitParamDecl(self, ast: ParamDecl, param):  # name: str, typ: Type, out: bool = False, inherit: bool = False
        """ # Invalid(Parameter(), <parameter-name>)
            - when a parameter is declared in a function with no parent.
        """
        name = ast.name
        # self.symbolTable.checkRedeclare(name, Variable())
        param_type = self.visit(ast.typ, param)
        inherit = ast.inherit
        out = ast.out
        # auto -> check InValid Variable declaration
        return ParamType(name, param_type, inherit, out)


    def visitFuncCall(self, ast: FuncCall, param):  # name: str, args: List[Expr]
        # function call must have non-void return type, if not -> Type mismatch in expression
        # find
        func_scope = self.symbolTable.findSymbol(ast.name, Function(), lambda x: x, ast)
        if func_scope is None:
            # check redeclare in globali
            global_func =  self.lookup(name=ast.name, lst=self.global_envi, func= lambda x: x.name)
            if global_func is None:
                raise Undeclared(Function(), ast.name)
            else:
                # check type of globalenvi
                if not self.parsArgsSpecialFunMatchingCheck(ast.args,global_func.mtype.partype):
                    raise TypeMismatchInExpression(ast)
                elif TypeChecker.isVoid(global_func.mtype.rettype):
                    raise TypeMismatchInExpression(ast)
                else:
                    return global_func.mtype.rettype

        else:
            # check param
            rettyp = func_scope[ast.name].mtype.rettype
            func_param = func_scope[ast.name].mtype.partype
            func_args = ast.args
            # check param matching + return type (non-void)
            if not self.parsArgsMatchingCheck(func_args, func_param, ast.name) or TypeChecker.isVoid(rettyp):
                raise TypeMismatchInExpression(ast)

            return rettyp

    # Expression ##################################################
    def visitBinExpr(self, ast: BinExpr, param):  # op: str, left: Expr, right: Expr
        exprType = None
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)
        op = ast.op

        string_op = ['::']
        intFloat2BoolOp = ['<', '>', '<=', '>=']
        intFloatOp = ['-','+', '*', '/']
        intOp = ['%']
        boolOp = ['!', '&&', '||']
        intBool2BoolOp = ['==', '!=']

        if op in string_op:
            if TypeChecker.isAuto(left_type):
                if TypeChecker.isFuncCall(ast.left):
                    self.symbolTable.inferType(ast.left.name, StringType(), True)
                elif TypeChecker.isId(ast.left):
                    self.symbolTable.inferType(ast.left.name, StringType(), False)
                left_type = StringType()

            if TypeChecker.isAuto(right_type):
                if TypeChecker.isFuncCall(ast.right):
                    self.symbolTable.inferType(ast.right.name, StringType(), True)
                elif TypeChecker.isId(ast.right):
                    self.symbolTable.inferType(ast.right.name, StringType(), False)
                right_type = StringType()

            if not TypeChecker.isStringType(left_type) or not TypeChecker.isStringType(right_type):
                raise TypeMismatchInExpression(ast)
            return StringType()

        elif op in intOp:
            if TypeChecker.isAuto(left_type):
                if TypeChecker.isFuncCall(ast.left):
                    self.symbolTable.inferType(ast.left.name, IntegerType(), True)
                elif TypeChecker.isId(ast.left):
                    self.symbolTable.inferType(ast.left.name, IntegerType(), False)
                left_type = IntegerType()

            if TypeChecker.isAuto(right_type):
                if TypeChecker.isFuncCall(ast.right):
                    self.symbolTable.inferType(ast.right.name, IntegerType(), True)
                elif TypeChecker.isId(ast.right):
                    self.symbolTable.inferType(ast.right.name, IntegerType(), False)
                right_type = IntegerType()

            if not TypeChecker.isIntType(left_type) or not TypeChecker.isIntType(right_type):
                raise TypeMismatchInExpression(ast)
            # print("eval: ", eval(f'{ast.left.val}{ast.op}{ast.right.val}'))
            return IntegerType()

        elif op in boolOp:
            if TypeChecker.isAuto(left_type):
                if TypeChecker.isFuncCall(ast.left):
                    self.symbolTable.inferType(ast.left.name, BooleanType(), True)
                elif TypeChecker.isId(ast.left):
                    self.symbolTable.inferType(ast.left.name, BooleanType(), False)
                left_type = BooleanType()

            if TypeChecker.isAuto(right_type):
                if TypeChecker.isFuncCall(ast.right):
                    self.symbolTable.inferType(ast.right.name, BooleanType(), True)
                elif TypeChecker.isId(ast.right):
                    self.symbolTable.inferType(ast.right.name, BooleanType(), False)
                right_type = BooleanType()

            if not TypeChecker.isBoolType(left_type) or not TypeChecker.isBoolType(right_type):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        elif op in intBool2BoolOp:
            if TypeChecker.isAuto(left_type):
                if TypeChecker.isFuncCall(ast.left):
                    if TypeChecker.isAuto(right_type):
                        self.symbolTable.inferType(ast.left.name, BooleanType(), True)
                        left_type = BooleanType()
                    else:
                        self.symbolTable.inferType(ast.left.name, right_type, True)
                        left_type = right_type
                elif TypeChecker.isId(ast.left):
                    if TypeChecker.isAuto(right_type):
                        self.symbolTable.inferType(ast.left.name, BooleanType(), False)
                        left_type = BooleanType()
                    else:
                        self.symbolTable.inferType(ast.left.name, right_type, False)
                        left_type = right_type

            if TypeChecker.isAuto(right_type):
                if TypeChecker.isFuncCall(ast.right):
                    if TypeChecker.isAuto(left_type):
                        self.symbolTable.inferType(ast.right.name, BooleanType(), True)
                        right_type = BooleanType()
                    else:
                        self.symbolTable.inferType(ast.right.name, left_type, True)
                        right_type = left_type
                elif TypeChecker.isId(ast.right):
                    if TypeChecker.isAuto(left_type):
                        self.symbolTable.inferType(ast.right.name, BooleanType(), False)
                        right_type = BooleanType()
                    else:
                        self.symbolTable.inferType(ast.right.name, left_type, False)
                        right_type = left_type

            if not TypeChecker.isInListOfType(left_type, [IntegerType, BooleanType]) or not TypeChecker.isInListOfType(right_type, [IntegerType, BooleanType]):
                raise TypeMismatchInExpression(ast)
            return BooleanType()

        elif op in intFloatOp:
            if TypeChecker.isAuto(left_type):
                if TypeChecker.isFuncCall(ast.left):
                    if TypeChecker.isAuto(right_type):
                        self.symbolTable.inferType(ast.left.name, FloatType(), True)
                        left_type = FloatType()
                    else:
                        self.symbolTable.inferType(ast.left.name, right_type, True)
                        left_type = right_type
                elif TypeChecker.isId(ast.left):
                    if TypeChecker.isAuto(right_type):
                        self.symbolTable.inferType(ast.left.name, FloatType(), False)
                        left_type = FloatType()
                    else:
                        self.symbolTable.inferType(ast.left.name, right_type, False)
                        left_type = right_type

            if TypeChecker.isAuto(right_type):
                if TypeChecker.isFuncCall(ast.right):
                    if TypeChecker.isAuto(left_type):
                        self.symbolTable.inferType(ast.right.name, FloatType(), True)
                        right_type = FloatType()
                    elif TypeChecker.isInListOfType(left_type, [IntegerType, BooleanType]):
                        self.symbolTable.inferType(ast.right.name, left_type, True)
                        right_type = left_type
                elif TypeChecker.isId(ast.right):
                    if TypeChecker.isAuto(left_type):
                        self.symbolTable.inferType(ast.right.name, FloatType(), False)
                        right_type = FloatType()
                    else:
                        self.symbolTable.inferType(ast.right.name, left_type, False)
                        right_type = left_type


            if not TypeChecker.isInListOfType(left_type, [IntegerType, FloatType]) or not TypeChecker.isInListOfType(right_type, [IntegerType, FloatType]):
                raise TypeMismatchInExpression(ast)
            return FloatType() if TypeChecker.isFloatType(left_type) or TypeChecker.isFloatType(right_type) else IntegerType()

        elif op in intFloat2BoolOp:
            if TypeChecker.isAuto(left_type):
                if TypeChecker.isFuncCall(ast.left):
                    if TypeChecker.isAuto(right_type):
                        self.symbolTable.inferType(ast.left.name, FloatType(), True)
                        left_type = FloatType()
                    elif TypeChecker.isInListOfType(right_type, [IntegerType, FloatType]):
                        self.symbolTable.inferType(ast.left.name, right_type, True)
                        left_type = right_type
                elif TypeChecker.isId(ast.left):
                    if TypeChecker.isAuto(right_type):
                        self.symbolTable.inferType(ast.left.name, FloatType(), False)
                        left_type = FloatType()
                    else:
                        self.symbolTable.inferType(ast.left.name, right_type, False)
                        left_type = right_type

            if TypeChecker.isAuto(right_type):
                if TypeChecker.isFuncCall(ast.right):
                    if TypeChecker.isAuto(left_type):
                        self.symbolTable.inferType(ast.right.name, FloatType(), True)
                        right_type = FloatType()
                    elif TypeChecker.isInListOfType(left_type, [IntegerType, FloatType]):
                        self.symbolTable.inferType(ast.right.name, left_type, True)
                        right_type = left_type
                elif TypeChecker.isId(ast.right):
                    if TypeChecker.isAuto(left_type):
                        self.symbolTable.inferType(ast.right.name, BooleanType(), False)
                        right_type = FloatType()
                    else:
                        self.symbolTable.inferType(ast.right.name, left_type, False)
                        right_type = left_type
            if not TypeChecker.isInListOfType(left_type, [IntegerType, FloatType]) or not TypeChecker.isInListOfType(right_type, [IntegerType, FloatType]):
                raise TypeMismatchInExpression(ast)
            return BooleanType()
        else:
            raise TypeMismatchInExpression(ast)

    def visitUnExpr(self, ast: UnExpr, param):  # op: str, val: Expr
        operand_type = self.visit(ast.val, param) # visit -> get Type
        op = ast.op

        lhs_type = param if type(param) in [FloatType, IntegerType] else None

        if op != '-' and op != '!':
            raise TypeMismatchInExpression(ast)
        elif op == '-' and not TypeChecker.isInListOfType(operand_type, [IntegerType, FloatType, AutoType]):
            raise TypeMismatchInExpression(ast)
        elif op == '!' and not TypeChecker.isBoolType(operand_type):
            raise TypeMismatchInExpression(ast)
        else:
            if TypeChecker.isFuncCall(ast.val) and TypeChecker.isAuto(operand_type):
                scope = self.symbolTable.findSymbol(ast.val.name, Function(), lambda x: x, ast)
                if op == '-':
                    scope[ast.val.name].mtype.rettype = operand_type = lhs_type if TypeChecker.isInListOfType(lhs_type, [FloatType,IntegerType]) else FloatType()
                elif op == '!':
                    scope[ast.val.name].mtype.rettype = operand_type = BooleanType()
            elif TypeChecker.isId(ast.val) and TypeChecker.isAuto(operand_type):
                scope = self.symbolTable.findSymbol(ast.val.name, Variable(), lambda x: x, ast)
                if op == '-':
                    scope[ast.val.name].mtype = operand_type = lhs_type if TypeChecker.isInListOfType(lhs_type, [FloatType,IntegerType]) else FloatType()
                elif op == '!':
                    scope[ast.val.name].mtype = operand_type = BooleanType()

            return operand_type

    # STMT ##################################################
    def visitAssignStmt(self, ast: AssignStmt, param):  # lhs: LHS, rhs: Expr
        """ Type mismatch in statement
            - the left-hand side can be in any type except void type and array type.
            - The right-hand side (RHS) is either in the same type as that of the LHS
            or in the type that can coerce to the LHS type.
        """

        # TODO: fix
        # if TypeChecker.isArrayCell(ast.lhs):
        #     raise TypeMismatchInStatement(ast)

        lhs_type = self.visit(ast.lhs, param)
        rhs_type = self.visit(ast.rhs, lhs_type)

        if TypeChecker.isVoid(lhs_type) or TypeChecker.isArrayType(lhs_type):
            raise TypeMismatchInStatement(ast)
        if TypeChecker.isAuto(lhs_type):
            if TypeChecker.isFuncCall(ast.lhs):
                self.symbolTable.inferType(ast.lhs.name, rhs_type, True)
            elif TypeChecker.isId(ast.lhs):
                self.symbolTable.inferType(ast.lhs.name, rhs_type, False)

            lhs_type = rhs_type

        if TypeChecker.isAuto(rhs_type):
            if TypeChecker.isFuncCall(ast.rhs):
                self.symbolTable.inferType(ast.rhs.name, lhs_type, True)
            elif TypeChecker.isId(ast.rhs):
                self.symbolTable.inferType(ast.rhs.name, lhs_type, False)
            rhs_type = lhs_type

        # print(lhs_type, rhs_type)
        if not TypeChecker.isTheSameType(lhs_type, rhs_type):
            raise TypeMismatchInStatement(ast)
        else:
            return ast

    def visitCallStmt(self, ast: CallStmt, param):  # name: str, args: List[Expr]
        """ Type mismatch in statement: For a call statement <function-name>(<args>)
            -  the callee must have void as return type
        """
        # find function in symbol table
        scope = self.symbolTable.findSymbol(ast.name, Function(), lambda x: x, ast, True)
        if scope == None:
            specialFun = self.lookup(name=ast.name, lst=self.global_envi, func= lambda x: x.name)
            if specialFun is None:
                raise Undeclared(Function(), ast.name)
            else:
                # check param of specialfun
                if not self.parsArgsSpecialFunMatchingCheck(ast.args, specialFun.mtype.partype):
                    raise TypeMismatchInStatement(ast)
                # elif not TypeChecker.isVoid(specialFun.mtype.rettype):
                #     raise TypeMismatchInStatement(ast)

        else:
            paramsType = scope[ast.name].mtype.partype

            # check number of arguments
            list_of_args = reduce(lambda acc,ele: acc + [ele], ast.args, [])
            if not self.parsArgsMatchingCheck(list_of_args, paramsType, ast.name):
                raise TypeMismatchInStatement(ast)

        # if not TypeChecker.isVoid(scope[ast.name].mtype.rettype):
        #     raise TypeMismatchInStatement(ast)
        return ast

    def visitBlockStmt(self, ast: BlockStmt, param):  # body: List[Stmt or VarDecl]
        if param[1] == True:  # param is isParam for merge those param to the function scope
            # self.symbolTable.mergeParamTable()
            if ast.body and TypeChecker.isCallStmt(ast.body[0]) and ast.body[0].name in ['super', 'preventDefault']:
                ast.body = ast.body[1:]
        else:
            self.symbolTable.enterScope()

        for stmt in ast.body:
            self.visit(stmt, (param[0], False))
        self.symbolTable.exitScope()
        return ast.body

    def visitIfStmt(self, ast: IfStmt, param):  # cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
        # Type mismatch in statement: The type of a conditional expression in an if/while/do-while statement must be boolean.
        cond = self.visit(ast.cond, param)
        if not TypeChecker.isBoolType(cond):
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, param)
        if ast.fstmt:
            self.visit(ast.fstmt, param)
        return ast


    def visitForStmt(self, ast: ForStmt, param):  # init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
        # Type mismatch in statement: In for statement, the type of a scalar variable, update expression must be integer
        scalar_var_type = self.visit(ast.init.lhs, param)
        upd_expr_type = self.visit(ast.upd, param)
        cond_type = self.visit(ast.cond, param)

        if TypeChecker.isAuto(scalar_var_type):
            self.symbolTable.inferType(ast.init.lhs.name, IntegerType(), False)
            scalar_var_type = IntegerType()
        if not TypeChecker.isIntType(scalar_var_type) or not TypeChecker.isIntType(upd_expr_type) or not TypeChecker.isBoolType(cond_type):
            raise TypeMismatchInStatement(ast)

        self.symbolTable.enterLoop()
        # stmt is stmt
        self.visit(ast.stmt, param)

        self.symbolTable.exitLoop()
        return ast

    def visitWhileStmt(self, ast: WhileStmt, param):  # cond: Expr, stmt: Stmt
        cond_type = self.visit(ast.cond, param)
        if not TypeChecker.isBoolType(cond_type):
            raise TypeMismatchInStatement(ast)

        self.symbolTable.enterLoop()
        self.visit(ast.stmt, param)

        self.symbolTable.exitLoop()
        return ast

    def visitDoWhileStmt(self, ast: DoWhileStmt, param):  # cond: Expr, stmt: BlockStmt
        self.symbolTable.enterLoop()
        self.visit(ast.stmt, param)
        cond_type = self.visit(ast.cond, param)
        if not TypeChecker.isBoolType(cond_type):
            raise TypeMismatchInStatement(ast)
        self.symbolTable.exitLoop()
        return ast
    def visitBreakStmt(self, ast: BreakStmt, param):
        """ MustInLoop(<statement>)
            - A break/continue statement must be inside directly or indirectly a loop otherwise the exception
        """
        if self.symbolTable.inLoop == 0:
            raise MustInLoop(ast)
        # self.symbolTable.inLoop -= 1
        return ast

    def visitContinueStmt(self, ast: ContinueStmt, param):
        """ MustInLoop(<statement>)
            - A break/continue statement must be inside directly or indirectly a loop otherwise the exception
        """
        if self.symbolTable.inLoop == 0:
            raise MustInLoop(ast)
        # self.symbolTable.inLoop -= 1
        return ast

    def visitReturnStmt(self, ast: ReturnStmt, param):
        """ Type mismatch in statement:
            For a return statement, the return expression can be considered as RHS of an implicit
            assignment whose LHS is the return type.
        """

        rhs_type = self.visit(ast.expr, param) if ast.expr else VoidType()

        # find a function in symbol table
        scope = self.symbolTable.findSymbol(param[0], Function(), lambda x: x, ast)
        lhs_type = scope[param[0]].mtype.rettype

        if self.isFunScope():
            if self.isFirstReturn() is True:
                self.visitReturnFirstTime()  # already check the first return stmt
                if TypeChecker.isAuto(lhs_type) and not TypeChecker.isAuto(rhs_type):
                    scope[param[0]].mtype.rettype = rhs_type
                    return ast
                elif TypeChecker.isAuto(rhs_type) and not TypeChecker.isAuto(lhs_type):
                    self.symbolTable.inferType(ast.expr.name, lhs_type,
                                               True if TypeChecker.isFuncCall(ast.expr) else False)

                if not TypeChecker.isTheSameType(lhs_type, rhs_type):
                    raise TypeMismatchInStatement(ast)

            else:
                return ast

        elif self.isInsideStmtScope():
            if TypeChecker.isAuto(lhs_type) and not TypeChecker.isAuto(rhs_type):
                scope[param[0]].mtype.rettype = rhs_type
                return ast
            elif TypeChecker.isAuto(rhs_type) and not TypeChecker.isAuto(lhs_type):
                self.symbolTable.inferType(ast.expr.name, lhs_type, True if TypeChecker.isFuncCall(ast.expr) else False)
            if not TypeChecker.isTheSameType(lhs_type, rhs_type):
                raise TypeMismatchInStatement(ast)
            return ast


        # if TypeChecker.isAuto(lhs_type) and not TypeChecker.isAuto(rhs_type):
        #     scope[param[0]].mtype.rettype = rhs_type
        #     return ast
        # elif TypeChecker.isAuto(rhs_type) and not TypeChecker.isAuto(lhs_type):
        #     self.symbolTable.inferType(ast.expr.name, lhs_type, True if TypeChecker.isFuncCall(ast.expr) else False)
        # else:
        #     if not TypeChecker.isTheSameType(lhs_type, rhs_type):
        #         raise TypeMismatchInStatement(ast)
        #     return ast

        # if not TypeChecker.isTheSameType(expr_type, self.symbolTable.returnType):
        #     raise TypeMismatchInStatement(ast)


    # Type ##################################################
    def visitIntegerType(self, ast, param):
        return IntegerType()

    def visitFloatType(self, ast, param):
        return FloatType()

    def visitBooleanType(self, ast, param):
        return BooleanType()

    def visitStringType(self, ast, param):
        return StringType()

    def visitAutoType(self, ast, param):
        return AutoType()

    def visitVoidType(self, ast, param):
        return VoidType()

    def visitArrayType(self, ast: ArrayType, param):
        return ast

    # Literal ##################################################
    def visitId(self, ast: Id, param):  # name: str
        id_scope = self.symbolTable.findSymbol(ast.name, Variable(), lambda x: x, ast)
        if id_scope is None:
            raise Undeclared(Identifier(), ast.name)
        return id_scope[ast.name].mtype

    def visitArrayCell(self, ast: ArrayCell, param):  # name: str, cell: List[Expr]
        # For an array subscripting (index operator) E1[E2], E1 must be in array type and E2 must
        # be a list of integer. If not, -> Type mismatch in expression
        # index must be >= 0
        scopeOfArray = self.symbolTable.findSymbol(ast.name, Variable(), lambda scope: scope, ast)
        if scopeOfArray is None:
            raise Undeclared(Identifier(), ast.name)
        elif not TypeChecker.isArrayType(scopeOfArray[ast.name].mtype):
            raise TypeMismatchInExpression(Id(ast.name))
        arrayType = scopeOfArray[ast.name].mtype

        indexList = []
        isFullIntLit = True
        # reduce(lambda _, ele: TypeMismatchInExpression(ast) if not TypeChecker.isIntType(self.visit(ele, param)) else None, ast.cell)
        for ele in ast.cell:
            index_type = self.visit(ele, param)
            if not TypeChecker.isIntType(index_type):
                raise TypeMismatchInExpression(ele)
            if isinstance(ele, IntegerLit):
                if ele.val < 0:
                    raise TypeMismatchInExpression(ele)
            else:
                isFullIntLit = False

            indexList += [ele]

        # check dimension
        dimenCheck = TypeChecker.arrayCellDimensCheck(indexList, arrayType.dimensions, isFullIntLit)
        arrayCellType = None
        if dimenCheck is False:
            raise TypeMismatchInExpression(ast)

        elif dimenCheck is True:
            arrayCellType = arrayType.typ
        else:
            arrayCellType = ArrayType(dimenCheck, arrayType.typ)

        return arrayCellType



    def visitArrayLit(self, ast: ArrayLit, param):
        """ IllegalArrayLiteral(<array literal>)
        - all literals in an array literal must be in the same type.
        """
        # get lsh type
        if TypeChecker.isArrayType(param):
            lsh_type = param.typ
        else:
            lsh_type = param

        first_type = None
        first_type = self.visit(ast.explist[0], param) if ast.explist else None

        if (lsh_type is None) and (not first_type is None):
            lsh_type = first_type
        elif (not lsh_type is None) and (TypeChecker.isAuto(first_type)):
            first_type = lsh_type

        for ele in ast.explist[1:]:
            ele_type = self.visit(ele, param)
            if TypeChecker.isAuto(ele_type):
                if TypeChecker.isFuncCall(ele):
                    self.symbolTable.inferType(ele.name, first_type, True)
                elif TypeChecker.isIntType(ele):
                    self.symbolTable.inferType(ele.name, first_type, False)
                    ele_type = first_type
            elif TypeChecker.isArrayType(ele_type):
                if TypeChecker.isTheSameType(first_type, ele_type) is False:
                    raise IllegalArrayLiteral(ast)
            elif not (type(ele_type) is type(first_type)):
                raise IllegalArrayLiteral(ast)

        retArrType = ArrayType([len(ast.explist)] + first_type.dimensions, first_type.typ) if TypeChecker.isArrayType(first_type) else ArrayType([len(ast.explist)], first_type)
        return retArrType

    def visitIntegerLit(self, ast: IntegerLit, param):
        return IntegerType()

    def visitFloatLit(self, ast: FloatLit, param):
        return FloatType()

    def visitStringLit(self, ast: StringLit, param):
        return StringType()

    def visitBooleanLit(self, ast: BooleanLit, param):
        return BooleanType()

###################################################

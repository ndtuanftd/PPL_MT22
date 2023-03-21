from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *
from functools import reduce
from itertools import zip_longest


# from src.main.mt22.utils.AST import VarDecl


class ASTGeneration(MT22Visitor):

    def toBool(self, x):
        return x == "true"

    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        decl_list = []
        for index in ctx.decl():
            decl = self.visit(index)  # visit DeclContext
            decl_list += decl
        return Program(decl_list)

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        if ctx.vardecl():
            res = self.visit(ctx.vardecl())
            return res
        else:
            return self.visit(ctx.fundecl())

    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        if ctx.vardecl_wo_asg():
            id_list, type = self.visit(ctx.vardecl_wo_asg())
            return list(map(lambda id: VarDecl(id, type, None), id_list))
        else:
            id_list, init_list, type = self.visit(ctx.vardecl_w_asg())
            return list(map(lambda lis: VarDecl(lis[0], type[0], lis[1]), zip(id_list[::-1], init_list)))

    def visitVardecl_wo_asg(self, ctx: MT22Parser.Vardecl_wo_asgContext):
        type = self.visit(ctx.varType())
        idlist = self.visit(ctx.idList())
        return idlist, type

    def visitVardecl_w_asg(self, ctx: MT22Parser.Vardecl_w_asgContext):
        if ctx.varType():  # ID COLON varType ASSIGN expr
            id = ctx.ID().getText()
            varType = self.visit(ctx.varType())
            expr = self.visit(ctx.expr())
            return ([id], [expr], [varType])
        else:  # ID COMMA vardecl_w_asg COMMA expr
            id = ctx.ID().getText()
            expr_temp = self.visit(ctx.expr())
            vardecl, expr, varType = self.visit(ctx.vardecl_w_asg())
            return ([*vardecl, id], [*expr, expr_temp], [*varType, None])

    def visitFundecl(self, ctx: MT22Parser.FundeclContext):
        # fun_prototype = self.visit(ctx.func_prototype())
        name = ctx.ID().getText()  # string
        return_type = self.visit(ctx.fnType())
        params = self.visit(ctx.paramdecl())
        inherit = self.visit(ctx.fun_inherit_subpart()) if ctx.fun_inherit_subpart() else None  # string or none
        body = self.visit(ctx.block_stm())
        # body = BlockStmt([VarDecl('a',IntegerType(), None)])
        return [FuncDecl(name, return_type, params, inherit, body)]

    # def visitVarType(self, ctx: MT22Parser.VarTypeContext):
    #     return

    # def visitFun_prototype(self, ctx: MT22Parser.Fun_prototypeContext):
    #     # ctx.fnType().accept(self)
    #     return None

    def visitFun_inherit_subpart(self, ctx: MT22Parser.Fun_inherit_subpartContext):
        """
        :param ctx:
        :return: should i return "function ID string" or "inherit string"
        """
        return ctx.ID().getText()

    def visitParamdecl(self, ctx: MT22Parser.ParamdeclContext):
        return self.visit(ctx.paramlist())

    def visitParamlist(self, ctx: MT22Parser.ParamlistContext):
        if ctx.params():
            return self.visit(ctx.params())
        else:
            return []

    def visitParams(self, ctx: MT22Parser.ParamsContext):
        """

        :param ctx:
        :return: list of ParamDecl
        """

        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else:
            return [self.visit(ctx.param())] + self.visit(ctx.params())
        # size = ctx.getChildCount()
        # res = [self.visit(ctx.param(0))]
        # print(f"Res {res}")
        # for i in range(1, size):
        #     res += [self.visit(ctx.param(i))]
        # return res

    def visitParam(self, ctx: MT22Parser.ParamContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.varType())
        out = True if ctx.OUT() else False
        inherit = True if ctx.INHERIT() else False
        return ParamDecl(name, typ, out, inherit)

    def visitStm(self, ctx: MT22Parser.StmContext):
        if ctx.ifStm():
            return self.visit(ctx.ifStm())
        elif ctx.agnStm():
            return self.visit(ctx.agnStm())
        elif ctx.forStm():
            return self.visit(ctx.forStm())
        elif ctx.block_stm():
            return self.visit(ctx.block_stm())
        elif ctx.whileStm():
            return self.visit(ctx.whileStm())
        elif ctx.doWhileStm():
            return self.visit(ctx.doWhileStm())
        elif ctx.breakStm():
            return self.visit(ctx.breakStm())
        elif ctx.continueStm():
            return self.visit(ctx.continueStm())
        elif ctx.returnStm():
            return self.visit(ctx.returnStm())
        else:
            return self.visit(ctx.callStm())

    def visitIfStm(self, ctx: MT22Parser.IfStmContext):
        cond = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stm())
        fstmt = self.visit(ctx.false_stm()) if ctx.false_stm() else None
        return IfStmt(cond, tstmt, fstmt)

    def visitFalse_stm(self, ctx: MT22Parser.False_stmContext):
        return self.visit(ctx.stm())

    def visitAgnStm(self, ctx: MT22Parser.AgnStmContext):
        # LHS: id or indexop
        lhs = Id(ctx.ID().getText()) if ctx.ID() else self.visit(ctx.indexOp())  # Id() is subclass of LHS
        # RHS: exprs
        rhs = self.visit(ctx.expr())
        return AssignStmt(lhs, rhs)

    def visitFunCall(self, ctx: MT22Parser.FunCallContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.exprList()) if ctx.exprList() else []
        return FuncCall(name, args)

    def visitForStm(self, ctx: MT22Parser.ForStmContext):
        init = AssignStmt(self.visit(ctx.scalar_variable()), self.visit(ctx.expr()))
        cond = self.visit(ctx.condition_expr())
        upd_expr = self.visit(ctx.update_expr())
        stmt = self.visit(ctx.stm())
        return ForStmt(init, cond, upd_expr, stmt)

    def visitScalar_variable(self, ctx: MT22Parser.Scalar_variableContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.indexOp())

    def visitCondition_expr(self, ctx: MT22Parser.Condition_exprContext):
        return self.visit(ctx.expr())

    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return self.visit(ctx.expr())

    def visitBlock_stm(self, ctx: MT22Parser.Block_stmContext):
        # stmts = [self.visit(item) for item in ctx.block_body()]
        if ctx.block_body():
            stmts = reduce(lambda acc, ele: acc + self.visit(ele), ctx.block_body()[1:], self.visit(ctx.block_body(0)))
            return BlockStmt(stmts)
        else:
            return BlockStmt([])

    def visitBlock_body(self, ctx: MT22Parser.Block_bodyContext):
        return [self.visit(ctx.stm())] if ctx.stm() else self.visit(ctx.vardecl())  # vardecl return list

    def visitWhileStm(self, ctx: MT22Parser.WhileStmContext):
        return WhileStmt(self.visit(ctx.condition_expr()), self.visit(ctx.stm()))

    def visitDoWhileStm(self, ctx: MT22Parser.DoWhileStmContext):
        return DoWhileStmt(self.visit(ctx.condition_expr()), self.visit(ctx.block_stm()))

    def visitBreakStm(self, ctx: MT22Parser.BreakStmContext):
        return BreakStmt()

    def visitContinueStm(self, ctx: MT22Parser.ContinueStmContext):
        return ContinueStmt()

    def visitReturnStm(self, ctx: MT22Parser.ReturnStmContext):
        return ReturnStmt(self.visit(ctx.expr()) if ctx.expr() else None)

    def visitCallStm(self, ctx: MT22Parser.CallStmContext):
        return CallStmt(ctx.ID().getText(), self.visit(ctx.exprList()) if ctx.exprList() else [])

    """
    Expression here
    """

    def visitExprList(self, ctx: MT22Parser.ExprListContext):
        # return [self.visit(item) for item in ctx.expr()]
        if (ctx.getChildCount() == 1):
            return [self.visit(ctx.expr())]
        else:
            return [self.visit(ctx.expr())] + self.visit(ctx.exprList())

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            # Bin(op, left, right)
            return BinExpr(ctx.STRINGCONCAT().getText(), self.visit(ctx.expr1(0)), self.visit(ctx.expr1(1)))

    def visitExpr1(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinExpr(self.visit(ctx.relational_op()), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))

    def visitExpr2(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.ANDOP():
            return BinExpr(ctx.ANDOP().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))
        else:
            return BinExpr(ctx.OROP().getText(), self.visit(ctx.expr2()), self.visit(ctx.expr3()))

    def visitExpr3(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.ADDOP():
            return BinExpr(ctx.ADDOP().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        else:
            return BinExpr(ctx.SUBOP().getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))

    def visitExpr4(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        elif ctx.MULOP():
            return BinExpr(ctx.MULOP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        elif ctx.DIVOP():
            return BinExpr(ctx.DIVOP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        else:
            return BinExpr(ctx.MODOP().getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))

    def visitExpr5(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            # print(ctx.NEGOP().getText())
            return UnExpr(ctx.NEGOP().getText(), self.visit(ctx.expr5()))

    def visitExpr6(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return UnExpr(ctx.SUBOP().getText(), self.visit(ctx.expr6()))

    def visitExpr7(self, ctx: MT22Parser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return self.visit(ctx.indexOp())

    def visitOperand(self, ctx: MT22Parser.OperandContext):
        if (ctx.INTLIT()):
            return IntegerLit(int(ctx.INTLIT().getText()))
        elif (ctx.FLOATLIT()):
            float_lit_str = ctx.FLOATLIT().getText()
            if float_lit_str[0] == '.':
                float_lit_str = '0' + float_lit_str
                # print(float_lit_str)
            return FloatLit(float(float_lit_str))
        elif (ctx.BOOLLIT()):
            # print(str(ctx.BOOLLIT().getText()))
            return BooleanLit(self.toBool(ctx.BOOLLIT().getText()))
        elif ctx.STRINGLIT():
            # print(ctx.STRINGLIT().getText())
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.arrLit():
            return self.visit(ctx.arrLit())
        elif ctx.funCall():
            return self.visit(ctx.funCall())
        elif ctx.indexOp():
            return self.visit(ctx.indexOp())
        else:
            return self.visit(ctx.expr())

    """
    END: Expression
    """

    def visitIdList(self, ctx: MT22Parser.IdListContext):
        # return [item.getText() for item in ctx.ID()]
        # res = [ctx.ID().getText()]
        # if ctx.getChildCount() == 1:
        #     return res
        # else:
        #     res += self.visit(ctx.idList())
        # return res
        # return [print(item.getText()) for item in ctx.ID()]
        if (ctx.getChildCount() == 1):
            return [ctx.ID().getText()]
        else:
            return [ctx.ID().getText()] + self.visit(ctx.idList())

    """ 
    Literal
    """

    def visitArrLit(self, ctx: MT22Parser.ArrLitContext):
        res = []
        if ctx.exprList():
            # print("ExprList()")
            res = self.visit(ctx.exprList())
            # print(res)
            # print("res: ", [item for item in res])
        return ArrayLit(res)

    def visitAtomicType(self, ctx: MT22Parser.AtomicTypeContext):
        if (ctx.INT()):
            return IntegerType()
        elif (ctx.FLOAT()):
            return FloatType()
        elif (ctx.BOOLEAN()):
            return BooleanType()
        else:
            return StringType()

    def visitVarType(self, ctx: MT22Parser.VarTypeContext):
        if ctx.atomicType():
            return self.visit(ctx.atomicType())
        elif ctx.AUTO():
            return AutoType()
        else:
            return self.visit(ctx.arrTypeDecl())

    def visitFnType(self, ctx: MT22Parser.FnTypeContext):
        if ctx.atomicType():
            return self.visit(ctx.atomicType())
        elif ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()
        else:
            return self.visit(ctx.arrTypeDecl())

    def visitArrTypeDecl(self, ctx: MT22Parser.ArrTypeDeclContext):
        # return self.visit(ctx.indexList()) + self.visit(ctx.atomicType())
        intList = list(map(lambda item: item.val, self.visit(ctx.exprList())))
        # [print(type(ele)) for ele in intList]
        return ArrayType(intList, self.visit(ctx.atomicType()))

    def visitIndexOp(self, ctx: MT22Parser.IndexOpContext):
        name = ctx.ID().getText()
        cell = self.visit(ctx.exprList())
        return ArrayCell(name, cell)

    def visitIndexList(self, ctx: MT22Parser.IndexListContext):
        size = ctx.getChildCount()
        res = [IntegerLit(int(ctx.INTLIT(0).getText()))]

        for i in range(1, size):
            res += [IntegerLit(int(ctx.INTLIT(i).getText()))]
        return res

    def visitRelational_op(self, ctx: MT22Parser.Relational_opContext):
        if ctx.EQOP():
            return ctx.EQOP().getText()
        elif ctx.NEQOP():
            return ctx.NEQOP().getText()
        elif ctx.LEOP():
            return ctx.LEOP().getText()
        elif ctx.GTOP():
            return ctx.GTOP().getText()
        elif ctx.LTOP():
            return ctx.LTOP().getText()
        else:
            return ctx.GEOP().getText()

    """
    END: Literal
    """

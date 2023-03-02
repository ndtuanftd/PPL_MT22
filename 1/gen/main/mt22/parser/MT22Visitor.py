# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/1/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_wo_asg.
    def visitVardecl_wo_asg(self, ctx:MT22Parser.Vardecl_wo_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl_w_asg.
    def visitVardecl_w_asg(self, ctx:MT22Parser.Vardecl_w_asgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fundecl.
    def visitFundecl(self, ctx:MT22Parser.FundeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fun_prototype.
    def visitFun_prototype(self, ctx:MT22Parser.Fun_prototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fun_inherit_subpart.
    def visitFun_inherit_subpart(self, ctx:MT22Parser.Fun_inherit_subpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdecl.
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stm.
    def visitStm(self, ctx:MT22Parser.StmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#agnStm.
    def visitAgnStm(self, ctx:MT22Parser.AgnStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifStm.
    def visitIfStm(self, ctx:MT22Parser.IfStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#matchStm.
    def visitMatchStm(self, ctx:MT22Parser.MatchStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#unMatchStm.
    def visitUnMatchStm(self, ctx:MT22Parser.UnMatchStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funCall.
    def visitFunCall(self, ctx:MT22Parser.FunCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forStm.
    def visitForStm(self, ctx:MT22Parser.ForStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_variable.
    def visitScalar_variable(self, ctx:MT22Parser.Scalar_variableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stm.
    def visitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whileStm.
    def visitWhileStm(self, ctx:MT22Parser.WhileStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#doWhileStm.
    def visitDoWhileStm(self, ctx:MT22Parser.DoWhileStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakStm.
    def visitBreakStm(self, ctx:MT22Parser.BreakStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continueStm.
    def visitContinueStm(self, ctx:MT22Parser.ContinueStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnStm.
    def visitReturnStm(self, ctx:MT22Parser.ReturnStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callStm.
    def visitCallStm(self, ctx:MT22Parser.CallStmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprList.
    def visitExprList(self, ctx:MT22Parser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr0.
    def visitExpr0(self, ctx:MT22Parser.Expr0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr1.
    def visitExpr1(self, ctx:MT22Parser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr2.
    def visitExpr2(self, ctx:MT22Parser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr3.
    def visitExpr3(self, ctx:MT22Parser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr4.
    def visitExpr4(self, ctx:MT22Parser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr5.
    def visitExpr5(self, ctx:MT22Parser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr6.
    def visitExpr6(self, ctx:MT22Parser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr7.
    def visitExpr7(self, ctx:MT22Parser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operand.
    def visitOperand(self, ctx:MT22Parser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idList.
    def visitIdList(self, ctx:MT22Parser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrLit.
    def visitArrLit(self, ctx:MT22Parser.ArrLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrEles.
    def visitArrEles(self, ctx:MT22Parser.ArrElesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_list.
    def visitInt_list(self, ctx:MT22Parser.Int_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#float_list.
    def visitFloat_list(self, ctx:MT22Parser.Float_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_list.
    def visitBool_list(self, ctx:MT22Parser.Bool_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_list.
    def visitString_list(self, ctx:MT22Parser.String_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomicType.
    def visitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#varType.
    def visitVarType(self, ctx:MT22Parser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fnType.
    def visitFnType(self, ctx:MT22Parser.FnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrTypeDecl.
    def visitArrTypeDecl(self, ctx:MT22Parser.ArrTypeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intOp.
    def visitIntOp(self, ctx:MT22Parser.IntOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#floatOp.
    def visitFloatOp(self, ctx:MT22Parser.FloatOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boolOp.
    def visitBoolOp(self, ctx:MT22Parser.BoolOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stringConcat.
    def visitStringConcat(self, ctx:MT22Parser.StringConcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexOp.
    def visitIndexOp(self, ctx:MT22Parser.IndexOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexList.
    def visitIndexList(self, ctx:MT22Parser.IndexListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#rUnaryOp.
    def visitRUnaryOp(self, ctx:MT22Parser.RUnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#binOp.
    def visitBinOp(self, ctx:MT22Parser.BinOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_op.
    def visitRelational_op(self, ctx:MT22Parser.Relational_opContext):
        return self.visitChildren(ctx)



del MT22Parser
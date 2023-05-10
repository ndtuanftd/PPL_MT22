# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/3/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete listener for a parse tree produced by MT22Parser.
class MT22Listener(ParseTreeListener):

    # Enter a parse tree produced by MT22Parser#program.
    def enterProgram(self, ctx:MT22Parser.ProgramContext):
        pass

    # Exit a parse tree produced by MT22Parser#program.
    def exitProgram(self, ctx:MT22Parser.ProgramContext):
        pass


    # Enter a parse tree produced by MT22Parser#decl.
    def enterDecl(self, ctx:MT22Parser.DeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#decl.
    def exitDecl(self, ctx:MT22Parser.DeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl.
    def enterVardecl(self, ctx:MT22Parser.VardeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl.
    def exitVardecl(self, ctx:MT22Parser.VardeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl_wo_asg.
    def enterVardecl_wo_asg(self, ctx:MT22Parser.Vardecl_wo_asgContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl_wo_asg.
    def exitVardecl_wo_asg(self, ctx:MT22Parser.Vardecl_wo_asgContext):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl_w_asg.
    def enterVardecl_w_asg(self, ctx:MT22Parser.Vardecl_w_asgContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl_w_asg.
    def exitVardecl_w_asg(self, ctx:MT22Parser.Vardecl_w_asgContext):
        pass


    # Enter a parse tree produced by MT22Parser#fundecl.
    def enterFundecl(self, ctx:MT22Parser.FundeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#fundecl.
    def exitFundecl(self, ctx:MT22Parser.FundeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#paramdecl.
    def enterParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#paramdecl.
    def exitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#paramlist.
    def enterParamlist(self, ctx:MT22Parser.ParamlistContext):
        pass

    # Exit a parse tree produced by MT22Parser#paramlist.
    def exitParamlist(self, ctx:MT22Parser.ParamlistContext):
        pass


    # Enter a parse tree produced by MT22Parser#params.
    def enterParams(self, ctx:MT22Parser.ParamsContext):
        pass

    # Exit a parse tree produced by MT22Parser#params.
    def exitParams(self, ctx:MT22Parser.ParamsContext):
        pass


    # Enter a parse tree produced by MT22Parser#param.
    def enterParam(self, ctx:MT22Parser.ParamContext):
        pass

    # Exit a parse tree produced by MT22Parser#param.
    def exitParam(self, ctx:MT22Parser.ParamContext):
        pass


    # Enter a parse tree produced by MT22Parser#fun_inherit_subpart.
    def enterFun_inherit_subpart(self, ctx:MT22Parser.Fun_inherit_subpartContext):
        pass

    # Exit a parse tree produced by MT22Parser#fun_inherit_subpart.
    def exitFun_inherit_subpart(self, ctx:MT22Parser.Fun_inherit_subpartContext):
        pass


    # Enter a parse tree produced by MT22Parser#stm.
    def enterStm(self, ctx:MT22Parser.StmContext):
        pass

    # Exit a parse tree produced by MT22Parser#stm.
    def exitStm(self, ctx:MT22Parser.StmContext):
        pass


    # Enter a parse tree produced by MT22Parser#agnStm.
    def enterAgnStm(self, ctx:MT22Parser.AgnStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#agnStm.
    def exitAgnStm(self, ctx:MT22Parser.AgnStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#ifStm.
    def enterIfStm(self, ctx:MT22Parser.IfStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#ifStm.
    def exitIfStm(self, ctx:MT22Parser.IfStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#false_stm.
    def enterFalse_stm(self, ctx:MT22Parser.False_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#false_stm.
    def exitFalse_stm(self, ctx:MT22Parser.False_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#funCall.
    def enterFunCall(self, ctx:MT22Parser.FunCallContext):
        pass

    # Exit a parse tree produced by MT22Parser#funCall.
    def exitFunCall(self, ctx:MT22Parser.FunCallContext):
        pass


    # Enter a parse tree produced by MT22Parser#forStm.
    def enterForStm(self, ctx:MT22Parser.ForStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#forStm.
    def exitForStm(self, ctx:MT22Parser.ForStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#scalar_variable.
    def enterScalar_variable(self, ctx:MT22Parser.Scalar_variableContext):
        pass

    # Exit a parse tree produced by MT22Parser#scalar_variable.
    def exitScalar_variable(self, ctx:MT22Parser.Scalar_variableContext):
        pass


    # Enter a parse tree produced by MT22Parser#condition_expr.
    def enterCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        pass

    # Exit a parse tree produced by MT22Parser#condition_expr.
    def exitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        pass


    # Enter a parse tree produced by MT22Parser#update_expr.
    def enterUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        pass

    # Exit a parse tree produced by MT22Parser#update_expr.
    def exitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        pass


    # Enter a parse tree produced by MT22Parser#block_stm.
    def enterBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#block_stm.
    def exitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#block_body.
    def enterBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        pass

    # Exit a parse tree produced by MT22Parser#block_body.
    def exitBlock_body(self, ctx:MT22Parser.Block_bodyContext):
        pass


    # Enter a parse tree produced by MT22Parser#whileStm.
    def enterWhileStm(self, ctx:MT22Parser.WhileStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#whileStm.
    def exitWhileStm(self, ctx:MT22Parser.WhileStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#doWhileStm.
    def enterDoWhileStm(self, ctx:MT22Parser.DoWhileStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#doWhileStm.
    def exitDoWhileStm(self, ctx:MT22Parser.DoWhileStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#breakStm.
    def enterBreakStm(self, ctx:MT22Parser.BreakStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#breakStm.
    def exitBreakStm(self, ctx:MT22Parser.BreakStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#continueStm.
    def enterContinueStm(self, ctx:MT22Parser.ContinueStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#continueStm.
    def exitContinueStm(self, ctx:MT22Parser.ContinueStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#returnStm.
    def enterReturnStm(self, ctx:MT22Parser.ReturnStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#returnStm.
    def exitReturnStm(self, ctx:MT22Parser.ReturnStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#callStm.
    def enterCallStm(self, ctx:MT22Parser.CallStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#callStm.
    def exitCallStm(self, ctx:MT22Parser.CallStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#exprList.
    def enterExprList(self, ctx:MT22Parser.ExprListContext):
        pass

    # Exit a parse tree produced by MT22Parser#exprList.
    def exitExprList(self, ctx:MT22Parser.ExprListContext):
        pass


    # Enter a parse tree produced by MT22Parser#expr.
    def enterExpr(self, ctx:MT22Parser.ExprContext):
        pass

    # Exit a parse tree produced by MT22Parser#expr.
    def exitExpr(self, ctx:MT22Parser.ExprContext):
        pass


    # Enter a parse tree produced by MT22Parser#expr1.
    def enterExpr1(self, ctx:MT22Parser.Expr1Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr1.
    def exitExpr1(self, ctx:MT22Parser.Expr1Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr2.
    def enterExpr2(self, ctx:MT22Parser.Expr2Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr2.
    def exitExpr2(self, ctx:MT22Parser.Expr2Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr3.
    def enterExpr3(self, ctx:MT22Parser.Expr3Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr3.
    def exitExpr3(self, ctx:MT22Parser.Expr3Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr4.
    def enterExpr4(self, ctx:MT22Parser.Expr4Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr4.
    def exitExpr4(self, ctx:MT22Parser.Expr4Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr5.
    def enterExpr5(self, ctx:MT22Parser.Expr5Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr5.
    def exitExpr5(self, ctx:MT22Parser.Expr5Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr6.
    def enterExpr6(self, ctx:MT22Parser.Expr6Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr6.
    def exitExpr6(self, ctx:MT22Parser.Expr6Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr7.
    def enterExpr7(self, ctx:MT22Parser.Expr7Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr7.
    def exitExpr7(self, ctx:MT22Parser.Expr7Context):
        pass


    # Enter a parse tree produced by MT22Parser#operand.
    def enterOperand(self, ctx:MT22Parser.OperandContext):
        pass

    # Exit a parse tree produced by MT22Parser#operand.
    def exitOperand(self, ctx:MT22Parser.OperandContext):
        pass


    # Enter a parse tree produced by MT22Parser#idList.
    def enterIdList(self, ctx:MT22Parser.IdListContext):
        pass

    # Exit a parse tree produced by MT22Parser#idList.
    def exitIdList(self, ctx:MT22Parser.IdListContext):
        pass


    # Enter a parse tree produced by MT22Parser#arrLit.
    def enterArrLit(self, ctx:MT22Parser.ArrLitContext):
        pass

    # Exit a parse tree produced by MT22Parser#arrLit.
    def exitArrLit(self, ctx:MT22Parser.ArrLitContext):
        pass


    # Enter a parse tree produced by MT22Parser#atomicType.
    def enterAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#atomicType.
    def exitAtomicType(self, ctx:MT22Parser.AtomicTypeContext):
        pass


    # Enter a parse tree produced by MT22Parser#varType.
    def enterVarType(self, ctx:MT22Parser.VarTypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#varType.
    def exitVarType(self, ctx:MT22Parser.VarTypeContext):
        pass


    # Enter a parse tree produced by MT22Parser#fnType.
    def enterFnType(self, ctx:MT22Parser.FnTypeContext):
        pass

    # Exit a parse tree produced by MT22Parser#fnType.
    def exitFnType(self, ctx:MT22Parser.FnTypeContext):
        pass


    # Enter a parse tree produced by MT22Parser#arrTypeDecl.
    def enterArrTypeDecl(self, ctx:MT22Parser.ArrTypeDeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#arrTypeDecl.
    def exitArrTypeDecl(self, ctx:MT22Parser.ArrTypeDeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#indexOp.
    def enterIndexOp(self, ctx:MT22Parser.IndexOpContext):
        pass

    # Exit a parse tree produced by MT22Parser#indexOp.
    def exitIndexOp(self, ctx:MT22Parser.IndexOpContext):
        pass


    # Enter a parse tree produced by MT22Parser#indexList.
    def enterIndexList(self, ctx:MT22Parser.IndexListContext):
        pass

    # Exit a parse tree produced by MT22Parser#indexList.
    def exitIndexList(self, ctx:MT22Parser.IndexListContext):
        pass


    # Enter a parse tree produced by MT22Parser#relational_op.
    def enterRelational_op(self, ctx:MT22Parser.Relational_opContext):
        pass

    # Exit a parse tree produced by MT22Parser#relational_op.
    def exitRelational_op(self, ctx:MT22Parser.Relational_opContext):
        pass


    # Enter a parse tree produced by MT22Parser#specialStm.
    def enterSpecialStm(self, ctx:MT22Parser.SpecialStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#specialStm.
    def exitSpecialStm(self, ctx:MT22Parser.SpecialStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#specialFunc.
    def enterSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        pass

    # Exit a parse tree produced by MT22Parser#specialFunc.
    def exitSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        pass


    # Enter a parse tree produced by MT22Parser#readIntStm.
    def enterReadIntStm(self, ctx:MT22Parser.ReadIntStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#readIntStm.
    def exitReadIntStm(self, ctx:MT22Parser.ReadIntStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#printIntStm.
    def enterPrintIntStm(self, ctx:MT22Parser.PrintIntStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#printIntStm.
    def exitPrintIntStm(self, ctx:MT22Parser.PrintIntStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#readFloatStm.
    def enterReadFloatStm(self, ctx:MT22Parser.ReadFloatStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#readFloatStm.
    def exitReadFloatStm(self, ctx:MT22Parser.ReadFloatStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#writeFloatStm.
    def enterWriteFloatStm(self, ctx:MT22Parser.WriteFloatStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#writeFloatStm.
    def exitWriteFloatStm(self, ctx:MT22Parser.WriteFloatStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#readBoolStm.
    def enterReadBoolStm(self, ctx:MT22Parser.ReadBoolStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#readBoolStm.
    def exitReadBoolStm(self, ctx:MT22Parser.ReadBoolStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#printBoolFn.
    def enterPrintBoolFn(self, ctx:MT22Parser.PrintBoolFnContext):
        pass

    # Exit a parse tree produced by MT22Parser#printBoolFn.
    def exitPrintBoolFn(self, ctx:MT22Parser.PrintBoolFnContext):
        pass


    # Enter a parse tree produced by MT22Parser#readStringStm.
    def enterReadStringStm(self, ctx:MT22Parser.ReadStringStmContext):
        pass

    # Exit a parse tree produced by MT22Parser#readStringStm.
    def exitReadStringStm(self, ctx:MT22Parser.ReadStringStmContext):
        pass


    # Enter a parse tree produced by MT22Parser#printStringFn.
    def enterPrintStringFn(self, ctx:MT22Parser.PrintStringFnContext):
        pass

    # Exit a parse tree produced by MT22Parser#printStringFn.
    def exitPrintStringFn(self, ctx:MT22Parser.PrintStringFnContext):
        pass


    # Enter a parse tree produced by MT22Parser#superFn.
    def enterSuperFn(self, ctx:MT22Parser.SuperFnContext):
        pass

    # Exit a parse tree produced by MT22Parser#superFn.
    def exitSuperFn(self, ctx:MT22Parser.SuperFnContext):
        pass


    # Enter a parse tree produced by MT22Parser#preventDefaultFn.
    def enterPreventDefaultFn(self, ctx:MT22Parser.PreventDefaultFnContext):
        pass

    # Exit a parse tree produced by MT22Parser#preventDefaultFn.
    def exitPreventDefaultFn(self, ctx:MT22Parser.PreventDefaultFnContext):
        pass



del MT22Parser
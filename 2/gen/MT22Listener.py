# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/2/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
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


    # Enter a parse tree produced by MT22Parser#decls.
    def enterDecls(self, ctx:MT22Parser.DeclsContext):
        pass

    # Exit a parse tree produced by MT22Parser#decls.
    def exitDecls(self, ctx:MT22Parser.DeclsContext):
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


    # Enter a parse tree produced by MT22Parser#vardecl1.
    def enterVardecl1(self, ctx:MT22Parser.Vardecl1Context):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl1.
    def exitVardecl1(self, ctx:MT22Parser.Vardecl1Context):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl2.
    def enterVardecl2(self, ctx:MT22Parser.Vardecl2Context):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl2.
    def exitVardecl2(self, ctx:MT22Parser.Vardecl2Context):
        pass


    # Enter a parse tree produced by MT22Parser#mid.
    def enterMid(self, ctx:MT22Parser.MidContext):
        pass

    # Exit a parse tree produced by MT22Parser#mid.
    def exitMid(self, ctx:MT22Parser.MidContext):
        pass


    # Enter a parse tree produced by MT22Parser#arrdecl.
    def enterArrdecl(self, ctx:MT22Parser.ArrdeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#arrdecl.
    def exitArrdecl(self, ctx:MT22Parser.ArrdeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#listInt.
    def enterListInt(self, ctx:MT22Parser.ListIntContext):
        pass

    # Exit a parse tree produced by MT22Parser#listInt.
    def exitListInt(self, ctx:MT22Parser.ListIntContext):
        pass


    # Enter a parse tree produced by MT22Parser#typ.
    def enterTyp(self, ctx:MT22Parser.TypContext):
        pass

    # Exit a parse tree produced by MT22Parser#typ.
    def exitTyp(self, ctx:MT22Parser.TypContext):
        pass


    # Enter a parse tree produced by MT22Parser#atomtyp.
    def enterAtomtyp(self, ctx:MT22Parser.AtomtypContext):
        pass

    # Exit a parse tree produced by MT22Parser#atomtyp.
    def exitAtomtyp(self, ctx:MT22Parser.AtomtypContext):
        pass


    # Enter a parse tree produced by MT22Parser#idlist.
    def enterIdlist(self, ctx:MT22Parser.IdlistContext):
        pass

    # Exit a parse tree produced by MT22Parser#idlist.
    def exitIdlist(self, ctx:MT22Parser.IdlistContext):
        pass


    # Enter a parse tree produced by MT22Parser#ids.
    def enterIds(self, ctx:MT22Parser.IdsContext):
        pass

    # Exit a parse tree produced by MT22Parser#ids.
    def exitIds(self, ctx:MT22Parser.IdsContext):
        pass


    # Enter a parse tree produced by MT22Parser#funcdecl.
    def enterFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#funcdecl.
    def exitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#parameter.
    def enterParameter(self, ctx:MT22Parser.ParameterContext):
        pass

    # Exit a parse tree produced by MT22Parser#parameter.
    def exitParameter(self, ctx:MT22Parser.ParameterContext):
        pass


    # Enter a parse tree produced by MT22Parser#listparam.
    def enterListparam(self, ctx:MT22Parser.ListparamContext):
        pass

    # Exit a parse tree produced by MT22Parser#listparam.
    def exitListparam(self, ctx:MT22Parser.ListparamContext):
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


    # Enter a parse tree produced by MT22Parser#expression.
    def enterExpression(self, ctx:MT22Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by MT22Parser#expression.
    def exitExpression(self, ctx:MT22Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by MT22Parser#relatexpr1.
    def enterRelatexpr1(self, ctx:MT22Parser.Relatexpr1Context):
        pass

    # Exit a parse tree produced by MT22Parser#relatexpr1.
    def exitRelatexpr1(self, ctx:MT22Parser.Relatexpr1Context):
        pass


    # Enter a parse tree produced by MT22Parser#relatexpr2.
    def enterRelatexpr2(self, ctx:MT22Parser.Relatexpr2Context):
        pass

    # Exit a parse tree produced by MT22Parser#relatexpr2.
    def exitRelatexpr2(self, ctx:MT22Parser.Relatexpr2Context):
        pass


    # Enter a parse tree produced by MT22Parser#logicexpr1.
    def enterLogicexpr1(self, ctx:MT22Parser.Logicexpr1Context):
        pass

    # Exit a parse tree produced by MT22Parser#logicexpr1.
    def exitLogicexpr1(self, ctx:MT22Parser.Logicexpr1Context):
        pass


    # Enter a parse tree produced by MT22Parser#addexpr.
    def enterAddexpr(self, ctx:MT22Parser.AddexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#addexpr.
    def exitAddexpr(self, ctx:MT22Parser.AddexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#multiexpr.
    def enterMultiexpr(self, ctx:MT22Parser.MultiexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#multiexpr.
    def exitMultiexpr(self, ctx:MT22Parser.MultiexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#logicexpr2.
    def enterLogicexpr2(self, ctx:MT22Parser.Logicexpr2Context):
        pass

    # Exit a parse tree produced by MT22Parser#logicexpr2.
    def exitLogicexpr2(self, ctx:MT22Parser.Logicexpr2Context):
        pass


    # Enter a parse tree produced by MT22Parser#signexpr.
    def enterSignexpr(self, ctx:MT22Parser.SignexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#signexpr.
    def exitSignexpr(self, ctx:MT22Parser.SignexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#indexexpr.
    def enterIndexexpr(self, ctx:MT22Parser.IndexexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#indexexpr.
    def exitIndexexpr(self, ctx:MT22Parser.IndexexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#op.
    def enterOp(self, ctx:MT22Parser.OpContext):
        pass

    # Exit a parse tree produced by MT22Parser#op.
    def exitOp(self, ctx:MT22Parser.OpContext):
        pass


    # Enter a parse tree produced by MT22Parser#subexpr.
    def enterSubexpr(self, ctx:MT22Parser.SubexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#subexpr.
    def exitSubexpr(self, ctx:MT22Parser.SubexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#funcCall.
    def enterFuncCall(self, ctx:MT22Parser.FuncCallContext):
        pass

    # Exit a parse tree produced by MT22Parser#funcCall.
    def exitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        pass


    # Enter a parse tree produced by MT22Parser#listargument.
    def enterListargument(self, ctx:MT22Parser.ListargumentContext):
        pass

    # Exit a parse tree produced by MT22Parser#listargument.
    def exitListargument(self, ctx:MT22Parser.ListargumentContext):
        pass


    # Enter a parse tree produced by MT22Parser#arguments.
    def enterArguments(self, ctx:MT22Parser.ArgumentsContext):
        pass

    # Exit a parse tree produced by MT22Parser#arguments.
    def exitArguments(self, ctx:MT22Parser.ArgumentsContext):
        pass


    # Enter a parse tree produced by MT22Parser#argument.
    def enterArgument(self, ctx:MT22Parser.ArgumentContext):
        pass

    # Exit a parse tree produced by MT22Parser#argument.
    def exitArgument(self, ctx:MT22Parser.ArgumentContext):
        pass


    # Enter a parse tree produced by MT22Parser#listexpr.
    def enterListexpr(self, ctx:MT22Parser.ListexprContext):
        pass

    # Exit a parse tree produced by MT22Parser#listexpr.
    def exitListexpr(self, ctx:MT22Parser.ListexprContext):
        pass


    # Enter a parse tree produced by MT22Parser#exprs.
    def enterExprs(self, ctx:MT22Parser.ExprsContext):
        pass

    # Exit a parse tree produced by MT22Parser#exprs.
    def exitExprs(self, ctx:MT22Parser.ExprsContext):
        pass


    # Enter a parse tree produced by MT22Parser#indexarr.
    def enterIndexarr(self, ctx:MT22Parser.IndexarrContext):
        pass

    # Exit a parse tree produced by MT22Parser#indexarr.
    def exitIndexarr(self, ctx:MT22Parser.IndexarrContext):
        pass


    # Enter a parse tree produced by MT22Parser#statement.
    def enterStatement(self, ctx:MT22Parser.StatementContext):
        pass

    # Exit a parse tree produced by MT22Parser#statement.
    def exitStatement(self, ctx:MT22Parser.StatementContext):
        pass


    # Enter a parse tree produced by MT22Parser#assignstate.
    def enterAssignstate(self, ctx:MT22Parser.AssignstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#assignstate.
    def exitAssignstate(self, ctx:MT22Parser.AssignstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#ifstate.
    def enterIfstate(self, ctx:MT22Parser.IfstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#ifstate.
    def exitIfstate(self, ctx:MT22Parser.IfstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#forstate.
    def enterForstate(self, ctx:MT22Parser.ForstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#forstate.
    def exitForstate(self, ctx:MT22Parser.ForstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#whilestate.
    def enterWhilestate(self, ctx:MT22Parser.WhilestateContext):
        pass

    # Exit a parse tree produced by MT22Parser#whilestate.
    def exitWhilestate(self, ctx:MT22Parser.WhilestateContext):
        pass


    # Enter a parse tree produced by MT22Parser#dowhilestate.
    def enterDowhilestate(self, ctx:MT22Parser.DowhilestateContext):
        pass

    # Exit a parse tree produced by MT22Parser#dowhilestate.
    def exitDowhilestate(self, ctx:MT22Parser.DowhilestateContext):
        pass


    # Enter a parse tree produced by MT22Parser#breakstate.
    def enterBreakstate(self, ctx:MT22Parser.BreakstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#breakstate.
    def exitBreakstate(self, ctx:MT22Parser.BreakstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#continuestate.
    def enterContinuestate(self, ctx:MT22Parser.ContinuestateContext):
        pass

    # Exit a parse tree produced by MT22Parser#continuestate.
    def exitContinuestate(self, ctx:MT22Parser.ContinuestateContext):
        pass


    # Enter a parse tree produced by MT22Parser#returnstate.
    def enterReturnstate(self, ctx:MT22Parser.ReturnstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#returnstate.
    def exitReturnstate(self, ctx:MT22Parser.ReturnstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#callstate.
    def enterCallstate(self, ctx:MT22Parser.CallstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#callstate.
    def exitCallstate(self, ctx:MT22Parser.CallstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#blockstate.
    def enterBlockstate(self, ctx:MT22Parser.BlockstateContext):
        pass

    # Exit a parse tree produced by MT22Parser#blockstate.
    def exitBlockstate(self, ctx:MT22Parser.BlockstateContext):
        pass


    # Enter a parse tree produced by MT22Parser#bodycontents.
    def enterBodycontents(self, ctx:MT22Parser.BodycontentsContext):
        pass

    # Exit a parse tree produced by MT22Parser#bodycontents.
    def exitBodycontents(self, ctx:MT22Parser.BodycontentsContext):
        pass


    # Enter a parse tree produced by MT22Parser#bodycontent.
    def enterBodycontent(self, ctx:MT22Parser.BodycontentContext):
        pass

    # Exit a parse tree produced by MT22Parser#bodycontent.
    def exitBodycontent(self, ctx:MT22Parser.BodycontentContext):
        pass


    # Enter a parse tree produced by MT22Parser#specialFunc.
    def enterSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        pass

    # Exit a parse tree produced by MT22Parser#specialFunc.
    def exitSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        pass


    # Enter a parse tree produced by MT22Parser#readInt.
    def enterReadInt(self, ctx:MT22Parser.ReadIntContext):
        pass

    # Exit a parse tree produced by MT22Parser#readInt.
    def exitReadInt(self, ctx:MT22Parser.ReadIntContext):
        pass


    # Enter a parse tree produced by MT22Parser#printInt.
    def enterPrintInt(self, ctx:MT22Parser.PrintIntContext):
        pass

    # Exit a parse tree produced by MT22Parser#printInt.
    def exitPrintInt(self, ctx:MT22Parser.PrintIntContext):
        pass


    # Enter a parse tree produced by MT22Parser#readFl.
    def enterReadFl(self, ctx:MT22Parser.ReadFlContext):
        pass

    # Exit a parse tree produced by MT22Parser#readFl.
    def exitReadFl(self, ctx:MT22Parser.ReadFlContext):
        pass


    # Enter a parse tree produced by MT22Parser#writeFl.
    def enterWriteFl(self, ctx:MT22Parser.WriteFlContext):
        pass

    # Exit a parse tree produced by MT22Parser#writeFl.
    def exitWriteFl(self, ctx:MT22Parser.WriteFlContext):
        pass


    # Enter a parse tree produced by MT22Parser#readBool.
    def enterReadBool(self, ctx:MT22Parser.ReadBoolContext):
        pass

    # Exit a parse tree produced by MT22Parser#readBool.
    def exitReadBool(self, ctx:MT22Parser.ReadBoolContext):
        pass


    # Enter a parse tree produced by MT22Parser#printBool.
    def enterPrintBool(self, ctx:MT22Parser.PrintBoolContext):
        pass

    # Exit a parse tree produced by MT22Parser#printBool.
    def exitPrintBool(self, ctx:MT22Parser.PrintBoolContext):
        pass


    # Enter a parse tree produced by MT22Parser#readStr.
    def enterReadStr(self, ctx:MT22Parser.ReadStrContext):
        pass

    # Exit a parse tree produced by MT22Parser#readStr.
    def exitReadStr(self, ctx:MT22Parser.ReadStrContext):
        pass


    # Enter a parse tree produced by MT22Parser#printStr.
    def enterPrintStr(self, ctx:MT22Parser.PrintStrContext):
        pass

    # Exit a parse tree produced by MT22Parser#printStr.
    def exitPrintStr(self, ctx:MT22Parser.PrintStrContext):
        pass


    # Enter a parse tree produced by MT22Parser#pFunc.
    def enterPFunc(self, ctx:MT22Parser.PFuncContext):
        pass

    # Exit a parse tree produced by MT22Parser#pFunc.
    def exitPFunc(self, ctx:MT22Parser.PFuncContext):
        pass


    # Enter a parse tree produced by MT22Parser#preventD.
    def enterPreventD(self, ctx:MT22Parser.PreventDContext):
        pass

    # Exit a parse tree produced by MT22Parser#preventD.
    def exitPreventD(self, ctx:MT22Parser.PreventDContext):
        pass



del MT22Parser
# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/2/src/main/mt22/parser\MT22.g4 by ANTLR 4.11.1
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


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl1.
    def visitVardecl1(self, ctx:MT22Parser.Vardecl1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl2.
    def visitVardecl2(self, ctx:MT22Parser.Vardecl2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#mid.
    def visitMid(self, ctx:MT22Parser.MidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrdecl.
    def visitArrdecl(self, ctx:MT22Parser.ArrdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listInt.
    def visitListInt(self, ctx:MT22Parser.ListIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomtyp.
    def visitAtomtyp(self, ctx:MT22Parser.AtomtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ids.
    def visitIds(self, ctx:MT22Parser.IdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listparam.
    def visitListparam(self, ctx:MT22Parser.ListparamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#params.
    def visitParams(self, ctx:MT22Parser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relatexpr1.
    def visitRelatexpr1(self, ctx:MT22Parser.Relatexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relatexpr2.
    def visitRelatexpr2(self, ctx:MT22Parser.Relatexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicexpr1.
    def visitLogicexpr1(self, ctx:MT22Parser.Logicexpr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#addexpr.
    def visitAddexpr(self, ctx:MT22Parser.AddexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiexpr.
    def visitMultiexpr(self, ctx:MT22Parser.MultiexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logicexpr2.
    def visitLogicexpr2(self, ctx:MT22Parser.Logicexpr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#signexpr.
    def visitSignexpr(self, ctx:MT22Parser.SignexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexexpr.
    def visitIndexexpr(self, ctx:MT22Parser.IndexexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#op.
    def visitOp(self, ctx:MT22Parser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpr.
    def visitSubexpr(self, ctx:MT22Parser.SubexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcCall.
    def visitFuncCall(self, ctx:MT22Parser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listargument.
    def visitListargument(self, ctx:MT22Parser.ListargumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arguments.
    def visitArguments(self, ctx:MT22Parser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#argument.
    def visitArgument(self, ctx:MT22Parser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#listexpr.
    def visitListexpr(self, ctx:MT22Parser.ListexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exprs.
    def visitExprs(self, ctx:MT22Parser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#indexarr.
    def visitIndexarr(self, ctx:MT22Parser.IndexarrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstate.
    def visitAssignstate(self, ctx:MT22Parser.AssignstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstate.
    def visitIfstate(self, ctx:MT22Parser.IfstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstate.
    def visitForstate(self, ctx:MT22Parser.ForstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestate.
    def visitWhilestate(self, ctx:MT22Parser.WhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestate.
    def visitDowhilestate(self, ctx:MT22Parser.DowhilestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstate.
    def visitBreakstate(self, ctx:MT22Parser.BreakstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestate.
    def visitContinuestate(self, ctx:MT22Parser.ContinuestateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstate.
    def visitReturnstate(self, ctx:MT22Parser.ReturnstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstate.
    def visitCallstate(self, ctx:MT22Parser.CallstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstate.
    def visitBlockstate(self, ctx:MT22Parser.BlockstateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodycontents.
    def visitBodycontents(self, ctx:MT22Parser.BodycontentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bodycontent.
    def visitBodycontent(self, ctx:MT22Parser.BodycontentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specialFunc.
    def visitSpecialFunc(self, ctx:MT22Parser.SpecialFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInt.
    def visitReadInt(self, ctx:MT22Parser.ReadIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInt.
    def visitPrintInt(self, ctx:MT22Parser.PrintIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFl.
    def visitReadFl(self, ctx:MT22Parser.ReadFlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFl.
    def visitWriteFl(self, ctx:MT22Parser.WriteFlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBool.
    def visitReadBool(self, ctx:MT22Parser.ReadBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBool.
    def visitPrintBool(self, ctx:MT22Parser.PrintBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readStr.
    def visitReadStr(self, ctx:MT22Parser.ReadStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printStr.
    def visitPrintStr(self, ctx:MT22Parser.PrintStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#pFunc.
    def visitPFunc(self, ctx:MT22Parser.PFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventD.
    def visitPreventD(self, ctx:MT22Parser.PreventDContext):
        return self.visitChildren(ctx)



del MT22Parser
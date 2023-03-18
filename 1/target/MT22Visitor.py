# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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


    # Visit a parse tree produced by MT22Parser#many_decl.
    def visitMany_decl(self, ctx:MT22Parser.Many_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_declare.
    def visitVar_declare(self, ctx:MT22Parser.Var_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl_body.
    def visitVar_decl_body(self, ctx:MT22Parser.Var_decl_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_list.
    def visitId_list(self, ctx:MT22Parser.Id_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#id_tail.
    def visitId_tail(self, ctx:MT22Parser.Id_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list.
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_tail.
    def visitExp_tail(self, ctx:MT22Parser.Exp_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function.
    def visitFunction(self, ctx:MT22Parser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_decl.
    def visitType_decl(self, ctx:MT22Parser.Type_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_typ.
    def visitArray_typ(self, ctx:MT22Parser.Array_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomic_typ.
    def visitAtomic_typ(self, ctx:MT22Parser.Atomic_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_typ.
    def visitVoid_typ(self, ctx:MT22Parser.Void_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_typ.
    def visitAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_decl.
    def visitPara_decl(self, ctx:MT22Parser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_list.
    def visitPara_list(self, ctx:MT22Parser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_tail.
    def visitPara_tail(self, ctx:MT22Parser.Para_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_list.
    def visitInt_list(self, ctx:MT22Parser.Int_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_tail.
    def visitInt_tail(self, ctx:MT22Parser.Int_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_list.
    def visitArray_list(self, ctx:MT22Parser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignment.
    def visitAssignment(self, ctx:MT22Parser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_stmt.
    def visitDo_stmt(self, ctx:MT22Parser.Do_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#cond_exp.
    def visitCond_exp(self, ctx:MT22Parser.Cond_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#spec_func.
    def visitSpec_func(self, ctx:MT22Parser.Spec_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_int.
    def visitRead_int(self, ctx:MT22Parser.Read_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_int.
    def visitPrint_int(self, ctx:MT22Parser.Print_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_float.
    def visitRead_float(self, ctx:MT22Parser.Read_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_float.
    def visitPrint_float(self, ctx:MT22Parser.Print_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_bool.
    def visitRead_bool(self, ctx:MT22Parser.Read_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_bool.
    def visitPrint_bool(self, ctx:MT22Parser.Print_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#read_string.
    def visitRead_string(self, ctx:MT22Parser.Read_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#print_string.
    def visitPrint_string(self, ctx:MT22Parser.Print_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sup.
    def visitSup(self, ctx:MT22Parser.SupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prevent_def.
    def visitPrevent_def(self, ctx:MT22Parser.Prevent_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_num.
    def visitExp_num(self, ctx:MT22Parser.Exp_numContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_boolean.
    def visitExp_boolean(self, ctx:MT22Parser.Exp_booleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_string.
    def visitExp_string(self, ctx:MT22Parser.Exp_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sub_exp.
    def visitSub_exp(self, ctx:MT22Parser.Sub_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index.
    def visitIndex(self, ctx:MT22Parser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call.
    def visitCall(self, ctx:MT22Parser.CallContext):
        return self.visitChildren(ctx)



del MT22Parser
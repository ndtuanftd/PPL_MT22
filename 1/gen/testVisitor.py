# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/1/playground\test.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .testParser import testParser
else:
    from testParser import testParser

# This class defines a complete generic visitor for a parse tree produced by testParser.

class testVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by testParser#prog.
    def visitProg(self, ctx:testParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#decl.
    def visitDecl(self, ctx:testParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#expr.
    def visitExpr(self, ctx:testParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#typeInt.
    def visitTypeInt(self, ctx:testParser.TypeIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#typeShort.
    def visitTypeShort(self, ctx:testParser.TypeShortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#typeLong.
    def visitTypeLong(self, ctx:testParser.TypeLongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#typeString.
    def visitTypeString(self, ctx:testParser.TypeStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#int.
    def visitInt(self, ctx:testParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#short.
    def visitShort(self, ctx:testParser.ShortContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#long.
    def visitLong(self, ctx:testParser.LongContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by testParser#string.
    def visitString(self, ctx:testParser.StringContext):
        return self.visitChildren(ctx)



del testParser
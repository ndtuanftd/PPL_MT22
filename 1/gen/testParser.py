# Generated from D:/DEV/HCMUT/222-work/PPL-ASGM/1/playground\test.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,61,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,4,0,19,8,0,11,0,12,0,20,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,2,1,2,1,2,3,2,34,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,42,
        8,2,10,2,12,2,45,9,2,1,3,1,3,1,3,1,3,3,3,51,8,3,1,4,1,4,1,5,1,5,
        1,6,1,6,1,7,1,7,1,7,0,1,4,8,0,2,4,6,8,10,12,14,0,0,60,0,18,1,0,0,
        0,2,24,1,0,0,0,4,33,1,0,0,0,6,50,1,0,0,0,8,52,1,0,0,0,10,54,1,0,
        0,0,12,56,1,0,0,0,14,58,1,0,0,0,16,19,3,2,1,0,17,19,3,4,2,0,18,16,
        1,0,0,0,18,17,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,
        21,22,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,5,9,0,0,25,26,5,1,
        0,0,26,27,5,11,0,0,27,28,5,2,0,0,28,29,5,10,0,0,29,3,1,0,0,0,30,
        31,6,2,-1,0,31,34,5,9,0,0,32,34,5,10,0,0,33,30,1,0,0,0,33,32,1,0,
        0,0,34,43,1,0,0,0,35,36,10,4,0,0,36,37,5,3,0,0,37,42,3,4,2,5,38,
        39,10,3,0,0,39,40,5,4,0,0,40,42,3,4,2,4,41,35,1,0,0,0,41,38,1,0,
        0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,5,1,0,0,0,45,43,
        1,0,0,0,46,51,3,8,4,0,47,51,3,10,5,0,48,51,3,12,6,0,49,51,3,14,7,
        0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,1,0,0,0,51,7,1,
        0,0,0,52,53,5,5,0,0,53,9,1,0,0,0,54,55,5,6,0,0,55,11,1,0,0,0,56,
        57,5,7,0,0,57,13,1,0,0,0,58,59,5,8,0,0,59,15,1,0,0,0,6,18,20,33,
        41,43,50
    ]

class testParser ( Parser ):

    grammarFileName = "test.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'", "'='", "'*'", "'+'", "'int'", "'short'", 
                     "'long'", "'string'", "<INVALID>", "<INVALID>", "'INT'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUM", "INT_TYPE", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_decl = 1
    RULE_expr = 2
    RULE_type = 3
    RULE_int = 4
    RULE_short = 5
    RULE_long = 6
    RULE_string = 7

    ruleNames =  [ "prog", "decl", "expr", "type", "int", "short", "long", 
                   "string" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    ID=9
    NUM=10
    INT_TYPE=11
    COMMENT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(testParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.DeclContext)
            else:
                return self.getTypedRuleContext(testParser.DeclContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.ExprContext)
            else:
                return self.getTypedRuleContext(testParser.ExprContext,i)


        def getRuleIndex(self):
            return testParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = testParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.decl()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.expr(0)
                    pass


                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==10):
                    break

            self.state = 22
            self.match(testParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(testParser.ID, 0)

        def INT_TYPE(self):
            return self.getToken(testParser.INT_TYPE, 0)

        def NUM(self):
            return self.getToken(testParser.NUM, 0)

        def getRuleIndex(self):
            return testParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = testParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(testParser.ID)
            self.state = 25
            self.match(testParser.T__0)
            self.state = 26
            self.match(testParser.INT_TYPE)
            self.state = 27
            self.match(testParser.T__1)
            self.state = 28
            self.match(testParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(testParser.ID, 0)

        def NUM(self):
            return self.getToken(testParser.NUM, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.ExprContext)
            else:
                return self.getTypedRuleContext(testParser.ExprContext,i)


        def getRuleIndex(self):
            return testParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = testParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 31
                self.match(testParser.ID)
                pass
            elif token in [10]:
                self.state = 32
                self.match(testParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 43
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 41
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = testParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        self.match(testParser.T__2)
                        self.state = 37
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = testParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        self.match(testParser.T__3)
                        self.state = 40
                        self.expr(4)
                        pass

             
                self.state = 45
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeIntContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_(self):
            return self.getTypedRuleContext(testParser.IntContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeInt" ):
                listener.enterTypeInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeInt" ):
                listener.exitTypeInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeInt" ):
                return visitor.visitTypeInt(self)
            else:
                return visitor.visitChildren(self)


    class TypeShortContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def short(self):
            return self.getTypedRuleContext(testParser.ShortContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeShort" ):
                listener.enterTypeShort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeShort" ):
                listener.exitTypeShort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeShort" ):
                return visitor.visitTypeShort(self)
            else:
                return visitor.visitChildren(self)


    class TypeStringContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(testParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeString" ):
                listener.enterTypeString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeString" ):
                listener.exitTypeString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeString" ):
                return visitor.visitTypeString(self)
            else:
                return visitor.visitChildren(self)


    class TypeLongContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def long(self):
            return self.getTypedRuleContext(testParser.LongContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLong" ):
                listener.enterTypeLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLong" ):
                listener.exitTypeLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeLong" ):
                return visitor.visitTypeLong(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = testParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = testParser.TypeIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.int_()
                pass
            elif token in [6]:
                localctx = testParser.TypeShortContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.short()
                pass
            elif token in [7]:
                localctx = testParser.TypeLongContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.long()
                pass
            elif token in [8]:
                localctx = testParser.TypeStringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.string()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)




    def int_(self):

        localctx = testParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(testParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_short

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShort" ):
                listener.enterShort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShort" ):
                listener.exitShort(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShort" ):
                return visitor.visitShort(self)
            else:
                return visitor.visitChildren(self)




    def short(self):

        localctx = testParser.ShortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(testParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LongContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_long

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLong" ):
                listener.enterLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLong" ):
                listener.exitLong(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLong" ):
                return visitor.visitLong(self)
            else:
                return visitor.visitChildren(self)




    def long(self):

        localctx = testParser.LongContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_long)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(testParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = testParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(testParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         





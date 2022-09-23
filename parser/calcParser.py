# Generated from calc.g4 by ANTLR 4.11.1
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
        4,1,10,56,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,5,
        0,14,8,0,10,0,12,0,17,9,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,2,
        1,2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,41,8,
        2,10,2,12,2,44,9,2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,52,8,4,1,5,1,5,1,
        5,0,1,4,6,0,2,4,6,8,10,0,0,55,0,15,1,0,0,0,2,24,1,0,0,0,4,32,1,0,
        0,0,6,45,1,0,0,0,8,51,1,0,0,0,10,53,1,0,0,0,12,14,3,2,1,0,13,12,
        1,0,0,0,14,17,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,1,1,0,0,0,17,
        15,1,0,0,0,18,19,3,4,2,0,19,20,3,10,5,0,20,25,1,0,0,0,21,22,3,6,
        3,0,22,23,3,10,5,0,23,25,1,0,0,0,24,18,1,0,0,0,24,21,1,0,0,0,25,
        3,1,0,0,0,26,27,6,2,-1,0,27,28,5,1,0,0,28,29,3,4,2,0,29,30,5,2,0,
        0,30,33,1,0,0,0,31,33,3,8,4,0,32,26,1,0,0,0,32,31,1,0,0,0,33,42,
        1,0,0,0,34,35,10,4,0,0,35,36,5,9,0,0,36,41,3,4,2,5,37,38,10,3,0,
        0,38,39,5,8,0,0,39,41,3,4,2,4,40,34,1,0,0,0,40,37,1,0,0,0,41,44,
        1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,5,1,0,0,0,44,42,1,0,0,0,45,
        46,5,10,0,0,46,47,5,3,0,0,47,48,3,4,2,0,48,7,1,0,0,0,49,52,5,6,0,
        0,50,52,5,7,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,9,1,0,0,0,53,54,5,
        4,0,0,54,11,1,0,0,0,6,15,24,32,40,42,51
    ]

class calcParser ( Parser ):

    grammarFileName = "calc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'='", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "INT", "FLOAT", "A_OP", "C_OP", 
                      "VARIABLE" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_assignment = 3
    RULE_num = 4
    RULE_line_end = 5

    ruleNames =  [ "prog", "stmt", "expr", "assignment", "num", "line_end" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WS=5
    INT=6
    FLOAT=7
    A_OP=8
    C_OP=9
    VARIABLE=10

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


        def getRuleIndex(self):
            return calcParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ProgramContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.StmtContext)
            else:
                return self.getTypedRuleContext(calcParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = calcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            localctx = calcParser.ProgramContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 1218) != 0:
                self.state = 12
                self.stmt()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calcParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExpressionContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)

        def line_end(self):
            return self.getTypedRuleContext(calcParser.Line_endContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)


    class StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignment(self):
            return self.getTypedRuleContext(calcParser.AssignmentContext,0)

        def line_end(self):
            return self.getTypedRuleContext(calcParser.Line_endContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = calcParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 24
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 6, 7]:
                localctx = calcParser.ExpressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 18
                self.expr(0)
                self.state = 19
                self.line_end()
                pass
            elif token in [10]:
                localctx = calcParser.StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.assignment()
                self.state = 22
                self.line_end()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def num(self):
            return self.getTypedRuleContext(calcParser.NumContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class ParenContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParen" ):
                listener.enterParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParen" ):
                listener.exitParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParen" ):
                return visitor.visitParen(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def A_OP(self):
            return self.getToken(calcParser.A_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(calcParser.ExprContext)
            else:
                return self.getTypedRuleContext(calcParser.ExprContext,i)

        def C_OP(self):
            return self.getToken(calcParser.C_OP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = calcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = calcParser.ParenContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 27
                self.match(calcParser.T__0)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(calcParser.T__1)
                pass
            elif token in [6, 7]:
                localctx = calcParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.num()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 42
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 40
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = calcParser.MulDivContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 35
                        localctx.op = self.match(calcParser.C_OP)
                        self.state = 36
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = calcParser.AddSubContext(self, calcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 38
                        localctx.op = self.match(calcParser.A_OP)
                        self.state = 39
                        self.expr(4)
                        pass

             
                self.state = 44
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(calcParser.VARIABLE, 0)

        def expr(self):
            return self.getTypedRuleContext(calcParser.ExprContext,0)


        def getRuleIndex(self):
            return calcParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = calcParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(calcParser.VARIABLE)
            self.state = 46
            self.match(calcParser.T__2)
            self.state = 47
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calcParser.RULE_num

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(calcParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(NumContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a calcParser.NumContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(calcParser.INT, 0)

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



    def num(self):

        localctx = calcParser.NumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_num)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = calcParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(calcParser.INT)
                pass
            elif token in [7]:
                localctx = calcParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(calcParser.FLOAT)
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


    class Line_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return calcParser.RULE_line_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine_end" ):
                listener.enterLine_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine_end" ):
                listener.exitLine_end(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine_end" ):
                return visitor.visitLine_end(self)
            else:
                return visitor.visitChildren(self)




    def line_end(self):

        localctx = calcParser.Line_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_line_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(calcParser.T__3)
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
         





# Generated from calc.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete listener for a parse tree produced by calcParser.
class calcListener(ParseTreeListener):

    # Enter a parse tree produced by calcParser#program.
    def enterProgram(self, ctx:calcParser.ProgramContext):
        pass

    # Exit a parse tree produced by calcParser#program.
    def exitProgram(self, ctx:calcParser.ProgramContext):
        pass


    # Enter a parse tree produced by calcParser#expression.
    def enterExpression(self, ctx:calcParser.ExpressionContext):
        pass

    # Exit a parse tree produced by calcParser#expression.
    def exitExpression(self, ctx:calcParser.ExpressionContext):
        pass


    # Enter a parse tree produced by calcParser#statement.
    def enterStatement(self, ctx:calcParser.StatementContext):
        pass

    # Exit a parse tree produced by calcParser#statement.
    def exitStatement(self, ctx:calcParser.StatementContext):
        pass


    # Enter a parse tree produced by calcParser#number.
    def enterNumber(self, ctx:calcParser.NumberContext):
        pass

    # Exit a parse tree produced by calcParser#number.
    def exitNumber(self, ctx:calcParser.NumberContext):
        pass


    # Enter a parse tree produced by calcParser#paren.
    def enterParen(self, ctx:calcParser.ParenContext):
        pass

    # Exit a parse tree produced by calcParser#paren.
    def exitParen(self, ctx:calcParser.ParenContext):
        pass


    # Enter a parse tree produced by calcParser#addSub.
    def enterAddSub(self, ctx:calcParser.AddSubContext):
        pass

    # Exit a parse tree produced by calcParser#addSub.
    def exitAddSub(self, ctx:calcParser.AddSubContext):
        pass


    # Enter a parse tree produced by calcParser#mulDiv.
    def enterMulDiv(self, ctx:calcParser.MulDivContext):
        pass

    # Exit a parse tree produced by calcParser#mulDiv.
    def exitMulDiv(self, ctx:calcParser.MulDivContext):
        pass


    # Enter a parse tree produced by calcParser#assignment.
    def enterAssignment(self, ctx:calcParser.AssignmentContext):
        pass

    # Exit a parse tree produced by calcParser#assignment.
    def exitAssignment(self, ctx:calcParser.AssignmentContext):
        pass


    # Enter a parse tree produced by calcParser#int.
    def enterInt(self, ctx:calcParser.IntContext):
        pass

    # Exit a parse tree produced by calcParser#int.
    def exitInt(self, ctx:calcParser.IntContext):
        pass


    # Enter a parse tree produced by calcParser#float.
    def enterFloat(self, ctx:calcParser.FloatContext):
        pass

    # Exit a parse tree produced by calcParser#float.
    def exitFloat(self, ctx:calcParser.FloatContext):
        pass


    # Enter a parse tree produced by calcParser#line_end.
    def enterLine_end(self, ctx:calcParser.Line_endContext):
        pass

    # Exit a parse tree produced by calcParser#line_end.
    def exitLine_end(self, ctx:calcParser.Line_endContext):
        pass



del calcParser
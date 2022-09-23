# Generated from calc.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .calcParser import calcParser
else:
    from calcParser import calcParser

# This class defines a complete generic visitor for a parse tree produced by calcParser.

class calcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by calcParser#program.
    def visitProgram(self, ctx:calcParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#expression.
    def visitExpression(self, ctx:calcParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#statement.
    def visitStatement(self, ctx:calcParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#number.
    def visitNumber(self, ctx:calcParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#paren.
    def visitParen(self, ctx:calcParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#addSub.
    def visitAddSub(self, ctx:calcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#mulDiv.
    def visitMulDiv(self, ctx:calcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#assignment.
    def visitAssignment(self, ctx:calcParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#int.
    def visitInt(self, ctx:calcParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#float.
    def visitFloat(self, ctx:calcParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by calcParser#line_end.
    def visitLine_end(self, ctx:calcParser.Line_endContext):
        return self.visitChildren(ctx)



del calcParser
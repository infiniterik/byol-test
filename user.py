import sys
from antlr4 import *
from build.calcLexer import calcLexer
from build.calcParser import calcParser
from build.calcVisitor import calcVisitor

class CV(calcVisitor):
    functions = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    # Visit a parse tree produced by calcParser#program.
    def visitProgram(self, ctx:calcParser.ProgramContext):
        return [self.visit(x) for x in ctx.stmt()]
    # Visit a parse tree produced by calcParser#expression.
    def visitExpression(self, ctx:calcParser.ExpressionContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by calcParser#statement.
    def visitStatement(self, ctx:calcParser.StatementContext):
        return self.visit(ctx.assignment())
    # Visit a parse tree produced by calcParser#number.
    def visitNumber(self, ctx:calcParser.NumberContext):
        return self.visit(ctx.num())

    # Visit a parse tree produced by calcParser#paren.
    def visitParen(self, ctx:calcParser.ParenContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by calcParser#addSub.
    def visitAddSub(self, ctx:calcParser.AddSubContext):
        res = self.functions[ctx.A_OP().getText()](self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        return res

    # Visit a parse tree produced by calcParser#mulDiv.
    def visitMulDiv(self, ctx:calcParser.MulDivContext):
        res = self.functions[ctx.C_OP().getText()](self.visit(ctx.expr(0)), self.visit(ctx.expr(1)))
        return res;
    # Visit a parse tree produced by calcParser#assignment.
    def visitAssignment(self, ctx:calcParser.AssignmentContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by calcParser#int.
    def visitInt(self, ctx:calcParser.IntContext):
        return int(ctx.getText())
    # Visit a parse tree produced by calcParser#float.
    def visitFloat(self, ctx:calcParser.FloatContext):
        return float(ctx.getFloat())


    # Visit a parse tree produced by calcParser#line_end.
    def visitLine_end(self, ctx:calcParser.Line_endContext):
        return self.visitChildren(ctx) 

def run(f):
    input_stream = FileStream(f)
    lexer = calcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = calcParser(stream)
    tree = parser.prog()
    print(tree.getText().strip())
    calc = CV()
    print(">", calc.visit(tree))

if __name__ == "__main__":
    run("tests/01_addition.txt")
    run("tests/02_test2.txt")

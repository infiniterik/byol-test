grammar calc;

prog : (stmt)* # program ;
stmt : expr line_end # expression
     | assignment line_end # statement ;
expr : expr op=C_OP expr # mulDiv
     | expr op=A_OP expr # addSub
     | '(' expr ')' # paren
     | num # number
     ;
     
assignment :  VARIABLE '=' expr;
     
num  : INT # int
     | FLOAT # float
     ;
WS : [ \t\r\n]+ -> skip;
INT  : [0-9]+ ;

FLOAT  : [0-9]+'.'[0-9]+ ;
A_OP : '+' | '-' ; 
C_OP : '*' | '/' ;
line_end : '\n' ;

VARIABLE : CHAR NCHAR* ;
CHAR : [ぁ-んa-zA-Z_] ; 
NCHAR : CHAR | INT ;

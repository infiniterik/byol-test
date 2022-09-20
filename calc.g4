grammar calc;

prog : (expr NEWLINE)* ;
expr : INT OP INT
     | num
     | '(' expr ')'
     ;
     
assignment :  VARIABLE "=" expr;
     
num  : INT ;
NEWLINE : [\r\n]+;
INT  : [0-9]+ ;
OP   : ( '+' | '-' | '*' | '/' ) ;
VARIABLE : [a-zA-Z_][a-zA-Z0-9]* ;

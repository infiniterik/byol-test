grammar calc;

prog : (expr NEWLINE)* ;
expr : INT OP INT
     | num
     | '(' expr ')'
     ;
     
num  : INT ;
NEWLINE : [\r\n]+;
INT  : [0-9]+ ;
OP   : ( '+' | '-' | '*' | '/' ) ;

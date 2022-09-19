grammar calc;

prog : (expr NEWLINE)* ;
expr : INT OP INT
     | num
     | '(' content ')'
     ;
content : expr;
num  : INT ;
NEWLINE : [\r\n]+;
INT  : [0-9]+ ;
OP   : ( '+' | '-' | '*' | '/' ) ;
fragment OPEN : '(';
fragment CLOSE: ')';

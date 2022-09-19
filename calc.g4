grammar calc;

prog : (expr NEWLINE)* ;
expr : content
     | '(' content ')'
     ;
content : INT OP INT
     | num;
num  : INT ;
NEWLINE : [\r\n]+;
INT  : [0-9]+ ;
OP   : ( '+' | '-' | '*' | '/' ) ;
fragment OPEN : '(';
fragment CLOSE: ')';

grammar calc;

prog : (expr NEWLINE)* ;
expr : INT OP INT
     | num
     | OPEN expr CLOSE
     ;
num  : INT ;
NEWLINE : [\r\n]+;
INT  : [0-9]+ ;
OP   : ( '+' | '-' | '*' | '/' ) ;
OPEN : '(';
CLOSE: ')';

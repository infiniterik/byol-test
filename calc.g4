grammar calc;

prog : (expr NEWLINE)* ;
expr : '(' content ')'
     | content
     ;
content : INT
     | INT OP INT;
NEWLINE : [\r\n]+;
INT  : [0-9]+ ;
OP   : ( '+' | '-' | '*' | '/' ) ;
fragment OPEN : '(';
fragment CLOSE: ')';

lexer grammar reglaslexer;

// Reglas léxicas
TRUE : 'true';
FALSE : 'false';
INT : '-'? [0-9]+;
FLOAT : '-'? [0-9]+ '.' [0-9]+;
DATE : [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};
STRING : '"' (~["\\] | ESC)* '"';
URL : STRING;

WS : [ \t\r\n]+ -> skip;

fragment ESC : '\\' [\\/bfnrt];



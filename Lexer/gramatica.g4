grammar Arithmetic;

expression: term
    | expression '+' term
    | expression '-' term
    ;

term: NUMBER;

NUMBER: DIGIT+;
fragment DIGIT: [0-9];
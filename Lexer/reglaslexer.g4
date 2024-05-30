lexer grammar reglaslexer;

// Reglas léxicas
EMPRESAS: '"empresas":';
VERSION:  '"versión":';
FIRMA_DIGITAL: '"firma_digital":';
INGRESOS_ANUALES: '"ingresos_anuales":';
NOMBRE_EMPRESA: '"nombre_empresa":';
FUNDACION: '"fundación":';
PYME: '"pyme":';
LINK: '"link":';
DIRECCION: '"dirección":';
EDAD: '"edad":';
CARGO: '"cargo":';
SALARIO: '"salario":';
ACTIVO: '"activo":';
CONTRATACION: '"fecha_contratación":';
FECHA_INICIO: '"fecha_inicio":';
ESTADO: '"estado":';
FECHA_FIN: '"fecha_fin":';
CALLE: '"calle":';
CIUDAD: '"ciudad":';
DEPARTAMENTOS: '"departamentos":';
EMPLEADO_LISTA: '"empleados":';
SUBDEPARTAMENTOS_LISTA: '"subdepartamentos":';
PROYECTOS_LISTA: '"proyectos":';
NOMBRE: '"nombre":';
JEFE: '"jefe":';
ABRO_LLAVE: '{';
CIERRO_LLAVE: '}';
ABRO_CORCHETE: '[';
CIERRO_CORCHETE: ']';
COMA: ',';
NULL: 'null';

//TIPOS
TRUE : 'true';
FALSE : 'false';
INT : '-'? [0-9]+;
FLOAT : '-'? [0-9]+ '.' [0-9]+;
DATE : [0-9]{4} '-' [0-9]{2} '-' [0-9]{2};
STRING : '"' (~["\\] | ESC)* '"';
URL : STRING;
WS : [ \t\r\n]+ -> skip;
fragment ESC : '\\' [\\/bfnrt];
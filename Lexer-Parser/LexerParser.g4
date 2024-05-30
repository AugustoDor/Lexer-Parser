// Definición de la gramática para JSON específico
grammar LexerParser;

// Regla de inicio
json : t_json | WS;

// Reglas parser
t_json : ABRO_LLAVE t_contenido CIERRO_LLAVE;
t_contenido : t_empresas ( COMA t_version)? ( COMA t_firma_digital)?;
t_version : VERSION STRING;
t_firma_digital : FIRMA_DIGITAL STRING;
t_empresas : EMPRESAS ABRO_CORCHETE t_listaempresas CIERRO_CORCHETE;
t_listaempresas : t_empresa ( COMA t_listaempresas)?;
t_empresa : ABRO_LLAVE t_contenidoempresa CIERRO_LLAVE;
t_contenidoempresa : t_nombre_empresa COMA t_fundacion COMA (t_direccion COMA )? t_ingresos_anuales COMA t_pyme COMA (t_link COMA )? t_departamentos;
t_ingresos_anuales : INGRESOS_ANUALES FLOAT;
t_nombre_empresa : NOMBRE_EMPRESA STRING;
t_fundacion : FUNDACION INT;
t_pyme : PYME (TRUE | FALSE);
t_link : LINK URL;
t_direccion : DIRECCION t_tipo_direccion;
t_tipo_direccion : NULL | ABRO_LLAVE CIERRO_LLAVE | ABRO_CORCHETE CIERRO_CORCHETE | ABRO_LLAVE t_calle COMA t_ciudad COMA t_pais CIERRO_LLAVE;
t_calle : CALLE STRING;
t_ciudad : CIUDAD STRING;
t_pais : PAIS STRING;
t_departamentos : DEPARTAMENTOS ABRO_CORCHETE t_listadepartamentos CIERRO_CORCHETE;
t_listadepartamentos : t_departamento ( COMA t_listadepartamentos)?;
t_departamento : ABRO_LLAVE t_contenidodepartamento CIERRO_LLAVE;
t_contenidodepartamento : t_nombre COMA (t_jefe COMA )? t_subdepartamentos;
t_nombre : NOMBRE STRING;
t_jefe : JEFE STRING;
t_subdepartamentos : SUBDEPARTAMENTOS_LISTA ABRO_CORCHETE t_listasubdepartamentos CIERRO_CORCHETE;
t_listasubdepartamentos : t_subdepartamento ( COMA t_listasubdepartamentos)?;
t_subdepartamento : ABRO_LLAVE t_contenidosubdepartamentos CIERRO_LLAVE;
t_contenidosubdepartamentos : t_nombre COMA (t_jefe COMA )? t_empleados?;
t_empleados : EMPLEADO_LISTA (ABRO_CORCHETE t_listaempleados CIERRO_CORCHETE | ABRO_LLAVE CIERRO_LLAVE | ABRO_CORCHETE CIERRO_CORCHETE | NULL);
t_listaempleados : t_empleado ( COMA t_listaempleados)?;
t_empleado : ABRO_LLAVE t_contenidoempleado CIERRO_LLAVE;
t_contenidoempleado :  t_nombre COMA (t_edad? COMA )? t_cargo COMA t_salario COMA t_activo COMA t_fecha_contratacion ( COMA t_proyectos)?;
t_edad : EDAD INT;
t_cargo : CARGO STRING;
t_salario : SALARIO FLOAT;
t_activo : ACTIVO (TRUE | FALSE);
t_fecha_contratacion : FECHA_CONTRATACION DATE;
t_proyectos : PROYECTOS_LISTA (ABRO_CORCHETE t_listaproyectos CIERRO_CORCHETE | ABRO_LLAVE CIERRO_LLAVE | ABRO_CORCHETE CIERRO_CORCHETE | NULL);
t_listaproyectos : t_proyecto ( COMA t_listaproyectos)?;
t_proyecto : ABRO_LLAVE t_contenidoproyecto CIERRO_LLAVE;
t_contenidoproyecto : t_nombre COMA (t_estado COMA )? t_fecha_inicio ( COMA t_fecha_fin)?;
t_fecha_inicio : FECHA_INICIO DATE;
t_estado : ESTADO STRING;
t_fecha_fin : FECHA_FIN (DATE | NULL);

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
FECHA_CONTRATACION: '"fecha_contratación":';
FECHA_INICIO: '"fecha_inicio":';
ESTADO: '"estado":';
FECHA_FIN: '"fecha_fin":';
CALLE: '"calle":';
CIUDAD: '"ciudad":';
PAIS: '"pais":';
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
INT : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]+;
DIGIT : [0-9];
DATE : '"' DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT '-' DIGIT DIGIT '"';
STRING : '"' (~["\\] | ESC)* '"';
URL : STRING;
WS : [ \t\r\n]+ -> skip;
fragment ESC : '\\' [\\/bfnrt];
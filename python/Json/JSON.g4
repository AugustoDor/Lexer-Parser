// Definición de la gramática para JSON específico
grammar JSON;

// Regla de inicio
json : t_json | WS;

// Reglas parser
t_json : '{' t_contenido '}';
t_contenido : t_empresas ( ',' t_version)? ( ',' t_firma_digital)?;
t_version : '"version"' ':' t_string;
t_firma_digital : '"firma_digital"' ':' t_string;
t_empresas : '"empresas"' ':' '[' t_listaempresas ']';
t_listaempresas : t_empresa ( ',' t_listaempresas)?;
t_empresa : '{' t_contenidoempresa '}';
t_contenidoempresa : t_nombre_empresa ',' t_fundacion ',' (t_direccion ',' )? t_ingresos_anuales ',' t_pyme ',' (t_link ',' )? t_departamentos;
t_ingresos_anuales : '"ingresos_anuales"' ':' t_float;
t_nombre_empresa : '"nombre_empresa"' ':' t_string;
t_fundacion : '"fundacion"' ':' t_int;
t_pyme : '"pyme"' ':' t_bool;
t_link : '"link"' ':' t_url;
t_direccion : '"direccion"' ':' t_tipo_direccion;
t_tipo_direccion : '{' '}' | '[' ']' | '{' t_calle ',' t_ciudad ',' t_pais '}';
t_calle : '"calle"' ':' t_string;
t_ciudad : '"ciudad"' ':' t_string;
t_pais : '"pais"' ':' t_string;
t_departamentos : '"departamentos"' ':' '[' t_listadepartamentos ']';
t_listadepartamentos : t_departamento ( ',' t_listadepartamentos)?;
t_departamento : '{' t_contenidodepartamento '}';
t_contenidodepartamento : t_nombre ',' (t_jefe ',' )? t_subdepartamentos;
t_nombre : '"nombre"' ':' t_string;
t_jefe : '"jefe"' ':' t_string;
t_subdepartamentos : '[' t_listasubdepartamentos ']';
t_listasubdepartamentos : t_subdepartamento ( ',' t_listasubdepartamentos)?;
t_subdepartamento : '{' t_contenidosubdepartamentos '}';
t_contenidosubdepartamentos : t_nombre ',' (t_jefe ',' )? t_empleados?;
t_empleados : '[' t_listaempleados ']' | '[' ']';
t_listaempleados : t_empleado ( ',' t_listaempleados)?;
t_empleado : '{' t_contenidoempleado '}';
t_contenidoempleado :  t_nombre ',' (t_edad? ',' )? t_cargo ',' t_salario ',' t_activo ',' t_fecha_contratacion ( ',' t_proyectos)?;
t_edad : '"edad"' ':' t_int;
t_cargo : '"cargo"' ':' t_string;
t_salario : '"salario"' ':' t_float;
t_activo : '"activo"' ':' t_bool;
t_fecha_contratacion : 'fecha_contratacion' ':' t_date;
t_proyectos : '[' t_listaproyectos ']' | '[' ']';
t_listaproyectos : t_proyecto ( ',' t_listaproyectos)?;
t_proyecto : '{' t_contenidoproyecto '}';
t_contenidoproyecto : t_nombre ',' (t_estado ',' )? t_fecha_inicio ( ',' t_fecha_fin)?;
t_fecha_inicio : '"fecha_inicio"' ':' t_date;
t_estado : '"estado"' ':' t_string;
t_fecha_fin : '"fecha_fin"' ':' t_date;

//TIPOS
//booleano
t_bool : 'true' | 'false';
//entero
t_int : '-'? INT;
INT : '0' | [1-9] [0-9]*;
//float
t_float : FLOAT;
FLOAT : ('-'? DIGIT+ '.' DIGIT+);
//fecha
t_date : DIGIT DIGIT DIGIT DIGIT '-' DIGIT DIGIT '-' DIGIT DIGIT;
DIGIT : [0-9];
//string
t_string : STRING;
STRING : '"' (~["\\] | ESC)* '"';
ESC : '\\' [\\/bfnrt"];
//urls
t_url: STRING;
//espacios en blanco
WS : [ \t\r\n]+ -> skip;
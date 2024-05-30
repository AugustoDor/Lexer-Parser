// Generated from C:/Lexer-Parser/Parser/reglasparser.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link reglasparser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface reglasparserVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link reglasparser#json}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitJson(reglasparser.JsonContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_json}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_json(reglasparser.T_jsonContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_contenido}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_contenido(reglasparser.T_contenidoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_version}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_version(reglasparser.T_versionContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_firma_digital}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_firma_digital(reglasparser.T_firma_digitalContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_empresas}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_empresas(reglasparser.T_empresasContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_listaempresas}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_listaempresas(reglasparser.T_listaempresasContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_empresa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_empresa(reglasparser.T_empresaContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_contenidoempresa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_contenidoempresa(reglasparser.T_contenidoempresaContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_ingresos_anuales}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_ingresos_anuales(reglasparser.T_ingresos_anualesContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_nombre_empresa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_nombre_empresa(reglasparser.T_nombre_empresaContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_fundacion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_fundacion(reglasparser.T_fundacionContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_pyme}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_pyme(reglasparser.T_pymeContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_link}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_link(reglasparser.T_linkContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_direccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_direccion(reglasparser.T_direccionContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_tipo_direccion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_tipo_direccion(reglasparser.T_tipo_direccionContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_calle}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_calle(reglasparser.T_calleContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_ciudad}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_ciudad(reglasparser.T_ciudadContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_pais}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_pais(reglasparser.T_paisContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_departamentos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_departamentos(reglasparser.T_departamentosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_listadepartamentos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_listadepartamentos(reglasparser.T_listadepartamentosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_departamento}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_departamento(reglasparser.T_departamentoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_contenidodepartamento}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_contenidodepartamento(reglasparser.T_contenidodepartamentoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_nombre}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_nombre(reglasparser.T_nombreContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_jefe}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_jefe(reglasparser.T_jefeContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_subdepartamentos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_subdepartamentos(reglasparser.T_subdepartamentosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_listasubdepartamentos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_listasubdepartamentos(reglasparser.T_listasubdepartamentosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_subdepartamento}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_subdepartamento(reglasparser.T_subdepartamentoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_contenidosubdepartamentos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_contenidosubdepartamentos(reglasparser.T_contenidosubdepartamentosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_empleados}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_empleados(reglasparser.T_empleadosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_listaempleados}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_listaempleados(reglasparser.T_listaempleadosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_empleado}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_empleado(reglasparser.T_empleadoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_contenidoempleado}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_contenidoempleado(reglasparser.T_contenidoempleadoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_edad}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_edad(reglasparser.T_edadContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_cargo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_cargo(reglasparser.T_cargoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_salario}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_salario(reglasparser.T_salarioContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_activo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_activo(reglasparser.T_activoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_fecha_contratacion}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_fecha_contratacion(reglasparser.T_fecha_contratacionContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_proyectos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_proyectos(reglasparser.T_proyectosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_listaproyectos}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_listaproyectos(reglasparser.T_listaproyectosContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_proyecto}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_proyecto(reglasparser.T_proyectoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_contenidoproyecto}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_contenidoproyecto(reglasparser.T_contenidoproyectoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_fecha_inicio}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_fecha_inicio(reglasparser.T_fecha_inicioContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_estado}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_estado(reglasparser.T_estadoContext ctx);
	/**
	 * Visit a parse tree produced by {@link reglasparser#t_fecha_fin}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitT_fecha_fin(reglasparser.T_fecha_finContext ctx);
}
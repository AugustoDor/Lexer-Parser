# Generated from C:/Lexer-Parser/src/Gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GramaticaParser import GramaticaParser
else:
    from GramaticaParser import GramaticaParser

# This class defines a complete generic visitor for a parse tree produced by GramaticaParser.

class GramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GramaticaParser#json.
    def visitJson(self, ctx:GramaticaParser.JsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_json.
    def visitT_json(self, ctx:GramaticaParser.T_jsonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_contenido.
    def visitT_contenido(self, ctx:GramaticaParser.T_contenidoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_version.
    def visitT_version(self, ctx:GramaticaParser.T_versionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_firma_digital.
    def visitT_firma_digital(self, ctx:GramaticaParser.T_firma_digitalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_empresas.
    def visitT_empresas(self, ctx:GramaticaParser.T_empresasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_listaempresas.
    def visitT_listaempresas(self, ctx:GramaticaParser.T_listaempresasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_empresa.
    def visitT_empresa(self, ctx:GramaticaParser.T_empresaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_contenidoempresa.
    def visitT_contenidoempresa(self, ctx:GramaticaParser.T_contenidoempresaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_ingresos_anuales.
    def visitT_ingresos_anuales(self, ctx:GramaticaParser.T_ingresos_anualesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_nombre_empresa.
    def visitT_nombre_empresa(self, ctx:GramaticaParser.T_nombre_empresaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_fundacion.
    def visitT_fundacion(self, ctx:GramaticaParser.T_fundacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_pyme.
    def visitT_pyme(self, ctx:GramaticaParser.T_pymeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_link.
    def visitT_link(self, ctx:GramaticaParser.T_linkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_direccion.
    def visitT_direccion(self, ctx:GramaticaParser.T_direccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_tipo_direccion.
    def visitT_tipo_direccion(self, ctx:GramaticaParser.T_tipo_direccionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_calle.
    def visitT_calle(self, ctx:GramaticaParser.T_calleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_ciudad.
    def visitT_ciudad(self, ctx:GramaticaParser.T_ciudadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_pais.
    def visitT_pais(self, ctx:GramaticaParser.T_paisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_departamentos.
    def visitT_departamentos(self, ctx:GramaticaParser.T_departamentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_listadepartamentos.
    def visitT_listadepartamentos(self, ctx:GramaticaParser.T_listadepartamentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_departamento.
    def visitT_departamento(self, ctx:GramaticaParser.T_departamentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_contenidodepartamento.
    def visitT_contenidodepartamento(self, ctx:GramaticaParser.T_contenidodepartamentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_nombre.
    def visitT_nombre(self, ctx:GramaticaParser.T_nombreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_jefe.
    def visitT_jefe(self, ctx:GramaticaParser.T_jefeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_subdepartamentos.
    def visitT_subdepartamentos(self, ctx:GramaticaParser.T_subdepartamentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_listasubdepartamentos.
    def visitT_listasubdepartamentos(self, ctx:GramaticaParser.T_listasubdepartamentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_subdepartamento.
    def visitT_subdepartamento(self, ctx:GramaticaParser.T_subdepartamentoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_contenidosubdepartamentos.
    def visitT_contenidosubdepartamentos(self, ctx:GramaticaParser.T_contenidosubdepartamentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_empleados.
    def visitT_empleados(self, ctx:GramaticaParser.T_empleadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_listaempleados.
    def visitT_listaempleados(self, ctx:GramaticaParser.T_listaempleadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_empleado.
    def visitT_empleado(self, ctx:GramaticaParser.T_empleadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_contenidoempleado.
    def visitT_contenidoempleado(self, ctx:GramaticaParser.T_contenidoempleadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_edad.
    def visitT_edad(self, ctx:GramaticaParser.T_edadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_cargo.
    def visitT_cargo(self, ctx:GramaticaParser.T_cargoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_salario.
    def visitT_salario(self, ctx:GramaticaParser.T_salarioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_activo.
    def visitT_activo(self, ctx:GramaticaParser.T_activoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_fecha_contratacion.
    def visitT_fecha_contratacion(self, ctx:GramaticaParser.T_fecha_contratacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_proyectos.
    def visitT_proyectos(self, ctx:GramaticaParser.T_proyectosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_listaproyectos.
    def visitT_listaproyectos(self, ctx:GramaticaParser.T_listaproyectosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_proyecto.
    def visitT_proyecto(self, ctx:GramaticaParser.T_proyectoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_contenidoproyecto.
    def visitT_contenidoproyecto(self, ctx:GramaticaParser.T_contenidoproyectoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_fecha_inicio.
    def visitT_fecha_inicio(self, ctx:GramaticaParser.T_fecha_inicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_estado.
    def visitT_estado(self, ctx:GramaticaParser.T_estadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GramaticaParser#t_fecha_fin.
    def visitT_fecha_fin(self, ctx:GramaticaParser.T_fecha_finContext):
        return self.visitChildren(ctx)



del GramaticaParser
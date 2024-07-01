
import os
from antlr4 import *
from GramáticaLexer import GramáticaLexer
from GramáticaParser import GramáticaParser
from GramáticaListener import GramáticaListener
from antlr4.error.ErrorListener import ErrorListener as ParserErrorListener

class CustomListener(GramáticaListener):
    def enterT_json(self, ctx):
        print("Entrando al JSON")

    def exitT_json(self, ctx):
        print("Saliendo del JSON")

    # Añade más métodos según las necesidades de tu proyecto

class ErrorListener(ParserErrorListener):
    def __init__(self):
        self.error = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.error = f"Error en Parser: {msg} en la linea {line}, y columna {column}"
        print(self.error)

class JSONToHTMLListener(GramáticaListener):
    def __init__(self):
        self.html = ""

    def enterT_json(self, ctx):
        self.html += "<html><body><h3>Data Analizada</h3>"

    def exitT_json(self, ctx):
        self.html += "</body></html>"

    def enterT_empresa(self, ctx):
        self.html += '<div style="border: 1px solid gray; padding: 20px;">'

    def exitT_empresa(self, ctx):
        self.html += "</div>"

    def enterT_version(self, ctx):
        self.html += f"<h4>Versión:{ctx.STRING().getText().strip('"')}</h4>"
    def exitT_version(self, ctx):
        pass

    def enterT_firma_digital(self, ctx):
        self.html += f"<h4>Firma digital:{ctx.STRING().getText().strip('"')}</h4>"
    def exitT_firma_digital(self, ctx):
        pass
    def enterT_nombre_empresa(self, ctx):
        self.html += f"<h1>{ctx.STRING().getText().strip('"')}</h1>"

    def exitT_nombre_empresa(self, ctx):
        pass

    def enterT_fundacion(self, ctx):
        self.html += f"<p>Fundación: {ctx.INT().getText()}</p>"

    def exitT_fundacion(self, ctx):
        pass

    def enterT_ingresos_anuales(self, ctx):
        self.html += f"<p>Ingresos Anuales: {ctx.FLOAT().getText().strip('"')}</p>"

    def exitT_ingresos_anuales(self, ctx):
        pass

    def enterT_pyme(self, ctx):
        pyme_value = "Sí" if ctx.children[1].getText() == "true" else "No"
        self.html += f"<p>PYME: {pyme_value}</p>"

    def exitT_pyme(self, ctx):
        pass

    def enterT_link(self, ctx):
        url = ctx.URL().getText().strip('"')
        self.html += f'<p>Link: <a href="{url}">{url}</a></p>'

    def exitT_link(self, ctx):
        pass

    def enterT_direccion(self, ctx):
        self.html += "<p>Dirección: <ul>"
        calle = ctx.t_tipo_direccion().t_calle().STRING().getText().strip('"')
        ciudad = ctx.t_tipo_direccion().t_ciudad().STRING().getText().strip('"')
        pais = ctx.t_tipo_direccion().t_pais().STRING().getText().strip('"')
        self.html += f"<li>Calle: {calle}</li>"
        self.html += f"<li>Ciudad: {ciudad}</li>"
        self.html += f"<li>País: {pais}</li>"
        self.html += "</ul></p>"

    def exitT_direccion(self, ctx):
        pass

    def enterT_departamentos(self, ctx):
        self.html += "<h2>Departamentos:</h2>"

    def exitT_departamentos(self, ctx):
        pass

    def enterT_departamento(self, ctx):
        self.html += '<div style="margin-left: 20px;">'

    def exitT_departamento(self, ctx):
        self.html += "</div>"

    def enterT_nombre(self, ctx):
        self.html += f"<h2>{ctx.STRING().getText().strip('"')}</h2>"

    def exitT_nombre(self, ctx):
        pass

    def enterT_jefe(self, ctx):
        if ctx.STRING():
            self.html += f"<p>Jefe: {ctx.STRING().getText().strip('"')}</p>"
        elif ctx.NULL():
            self.html += "<p>Jefe: null</p>"

    def exitT_jefe(self, ctx):
        pass

    def enterT_subdepartamentos(self, ctx):
        self.html += "<h3>Subdepartamentos:</h3>"

    def exitT_subdepartamentos(self, ctx):
        pass

    def enterT_empleados(self, ctx):
        self.html += "<ul>"

    def exitT_empleados(self, ctx):
        self.html += "</ul>"

    def enterT_empleado(self, ctx):
        self.html += "<li><div style='margin-left: 20px;'>"

    def exitT_empleado(self, ctx):
        self.html += "</div></li>"

    def enterT_edad(self, ctx):
        self.html += f"<p>Edad: {ctx.INT().getText()}</p>"

    def exitT_edad(self, ctx):
        pass

    def enterT_cargo(self, ctx):
        self.html += f"<p>Cargo: {ctx.TIPO_CARGO().getText().strip('"')}</p>"

    def exitT_cargo(self, ctx):
        pass

    def enterT_salario(self, ctx):
        if ctx.FLOAT():
            self.html += f"<p>Salario: {ctx.FLOAT().getText()}</p>"
        else:
            self.html += f"<p>Salario: {ctx.INT().getText()}</p>"

    def exitT_salario(self, ctx):
        pass

    def enterT_activo(self, ctx):
        activo_value = "Sí" if ctx.children[1].getText() == "true" else "No"
        self.html += f"<p>Activo: {activo_value}</p>"

    def exitT_activo(self, ctx):
        pass

    def enterT_fecha_contratacion(self, ctx):
        self.html += f"<p>Fecha de Contratación: {ctx.DATE().getText().strip('"')}</p>"

    def exitT_fecha_contratacion(self, ctx):
        pass

    def enterT_proyectos(self, ctx):
        self.html += "<h3>Proyectos:</h3>"

    def exitT_proyectos(self, ctx):
        pass

    def enterT_proyecto(self, ctx):
        self.html += "<table border='1'><tr><th>Estado</th><th>Fecha Inicio</th><th>Fecha de Fin</th></tr>"

    def exitT_proyecto(self, ctx):
        self.html += "</table>"

    def enterT_estado(self, ctx):
        if ctx.TIPO_ESTADO():
            self.html += f"<td>{ctx.TIPO_ESTADO().getText().strip('"')}</td>"
        else:
            self.html += f"<td>{ctx.NULL().getText().strip('"')}</td>"

    def exitT_estado(self, ctx):
        pass
    def enterT_fecha_inicio(self, ctx):
        self.html += f"<td>{ctx.DATE().getText().strip('"')}</td>"

    def exitT_fecha_inicio(self, ctx):
        pass

    def enterT_fecha_fin(self, ctx):
        self.html += f"<td>{ctx.DATE().getText().strip('"')}</td>"

    def exitT_fecha_fin(self, ctx):
        pass

def main():
    while True:
        file_name = input("Ingrese la ruta absoluta del archivo que desea analizar: ")
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                input_stream = InputStream(file.read())
                lexer = GramáticaLexer(input_stream)
                stream = CommonTokenStream(lexer)
                parser = GramáticaParser(stream)
                error_listener = ErrorListener()
                parser.addErrorListener(error_listener)
                tree = parser.json()

                script_dir = os.path.dirname(os.path.abspath(__file__))
                output_file_name = os.path.join(script_dir, f"{os.path.basename(file_name).rsplit('.', 1)[0]}.html")

                with open(output_file_name, "w", encoding='utf-8') as f:
                    if error_listener.error:
                        f.write(f"<html><body><h3>Se encontraron errores en el archivo de prueba</h3></body></html>")
                    else:
                        listener = JSONToHTMLListener()
                        walker = ParseTreeWalker()
                        walker.walk(listener, tree)
                        f.write(listener.html)

                if error_listener.error:
                    print(f"Errores encontrados: {error_listener.error}")
                else:
                    print(f"Parsing y traducción a HTML completado. Entrar a {output_file_name}")

        except FileNotFoundError:
            print(f"Archivo '{file_name}' no encontrado.")

        eleccion = input("¿Desea cargar otro archivo? (si/no): ").strip().lower()
        if eleccion != 'si':
            break

    input("Presiona Enter para salir...")

if __name__ == '__main__':
    main()
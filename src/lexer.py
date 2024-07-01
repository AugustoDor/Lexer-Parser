from antlr4 import *
from GramáticaLexer import GramáticaLexer
from GramáticaParser import GramáticaParser
from GramáticaListener import GramáticaListener


class CustomListener(GramáticaListener):
    def enterT_nombre_empresa(self, ctx):
        print(f"Nombre de la empresa: {ctx.getText()}")

    def enterT_fundacion(self, ctx):
        print(f"Fundación: {ctx.getText()}")

    def enterT_direccion(self, ctx):
        print(f"Dirección: {ctx.getText()}")

    def enterT_ingresos_anuales(self, ctx):
        print(f"Ingresos Anuales: {ctx.getText()}")

    def enterT_pyme(self, ctx):
        print(f"PYME: {ctx.getText()}")

    def enterT_departamentos(self, ctx):
        print(f"Departamentos: {ctx.getText()}")

    def enterT_empleado(self, ctx):
        print(f"Empleado: {ctx.getText()}")

    # Agrega más métodos si es necesario para manejar más detalles


def main():
    file_name = input("Ingrese la ruta absoluta del archivo que desea analizar: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            input_stream = InputStream(file.read())
            lexer = GramáticaLexer(input_stream)
            token_stream = CommonTokenStream(lexer)

            # Imprimir todos los tokens
            token_stream.fill()
            for token in token_stream.tokens:
                token_name = GramáticaLexer.symbolicNames[token.type]
                if token_name == 'ERROR':
                    print(f"Error: Token no reconocido '{token.text}' en la posición {token.start}")
                    break
                print(f'Token: {token.text}, Tipo: {token_name}, Línea: {token.line}, Columna: {token.column}')

            parser = GramáticaParser(token_stream)
            tree = parser.json()

            # Crear el listener y el walker
            listener = CustomListener()
            walker = ParseTreeWalker()
            walker.walk(listener, tree)

            print("Análisis completo.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
    input("Presiona Enter para salir...")


if __name__ == '__main__':
    main()

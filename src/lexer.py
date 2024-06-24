from antlr4 import *
from GramáticaLexer import GramáticaLexer


def main():
    file_name = input("Ingrese la ruta absoluta del archivo que desea analizar: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            input_stream = InputStream(file.read())
            lexer = GramáticaLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            token_stream.fill()
            for token in token_stream.tokens:
                token_name = GramáticaLexer.symbolicNames[token.type]
                if token_name == 'ERROR':  # Asegúrate de que 'ERROR' sea el nombre del token que indica un error
                    print(f"Error: Token no reconocido '{token.text}' en la posición {token.start}")
                    break
                print(f'Token: {token.text} Name: {token_name}')
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    input("Presiona Enter para salir...")


if __name__ == '__main__':
    main()

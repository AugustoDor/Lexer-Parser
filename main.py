from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser

"hola juan estoy probando"

def main():
    # Crear un InputStream para la entrada de texto
    input_stream = InputStream("hello w")
    # Crear el lexer a partir del InputStream
    lexer = HelloLexer(input_stream)
    # Crear un stream de tokens a partir del lexer
    stream = CommonTokenStream(lexer)
    # Crear el parser a partir del stream de tokens
    parser = HelloParser(stream)
    # Iniciar el parsing a partir de la regla inicial 'r'
    tree = parser.r()
    print(tree.toStringTree(recog=parser))

    # Obtener la lista de tokens generados por el lexer
    token_list = stream.tokens
    for token in token_list:
        print(f"Tipo: {lexer.symbolicNames[token.type]}, Texto: {token.text}, Posición: {token.line}:{token.column}")


if __name__ == '__main__':
    main()
import sys
from antlr4 import *
from reglaslexer import reglaslexer

def main():
    # Leer entrada desde un archivo o stdin
    input_stream = FileStream(sys.argv[1], encoding='utf-8') if len(sys.argv) > 1 else InputStream(sys.stdin.read())

    # Crear un lexer con la entrada
    lexer = reglaslexer(input_stream)

    # Obtener los tokens generados por el lexer
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    # Imprimir los tokens
    for token in token_stream.tokens:
        print(f"Token Type: {lexer.symbolicNames[token.type]}, Text: {token.text}")

if __name__ == '__main__':
    main()

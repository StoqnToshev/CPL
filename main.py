import lexer
import parser

def main():
    content = ""
    with open('test.cpl') as file:
        content = file.read()

    #lexer
    lex = lexer.Lexer(content)
    tokens = lex.tokenize()

    #parser
    parse = parser.Parser(tokens)
    obj = parse.parse()

main()
from parser import Parser

def main():
    Parser.tokens.origin = "2 + 3*3+  3"
    result = Parser.parse_expression()
    print(result)

if __name__ == "__main__":
    main()
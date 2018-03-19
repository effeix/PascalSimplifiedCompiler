from parser import Parser

def main():
    Parser.tokens.origin = "3+3)"
    result = Parser.parse()
    print(result)

if __name__ == "__main__":
    main()
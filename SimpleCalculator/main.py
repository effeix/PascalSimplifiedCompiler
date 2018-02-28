from parser import Parser

def main():
    Parser.tokens.origin = "1+2"
    result = Parser.parse()
    print(result)

if __name__ == "__main__":
    main()
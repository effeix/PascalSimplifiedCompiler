from parser import Parser

def main():
    Parser.tokens.origin = "111 *2   +35000000      -  2   +  51"
    result = Parser.parse()
    print(result)

if __name__ == "__main__":
    main()
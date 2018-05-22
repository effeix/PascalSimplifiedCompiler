from parser import Parser
from symboltable import SymbolTable


def read_pascal(f):
    with open(f, 'r') as ff:
        return ff.read().rstrip("\n")


def main(origin):
    st = SymbolTable(None)
    Parser.set_origin(origin.lower())
    parse = Parser.parse()
    parse.eval(st)


if __name__ == "__main__":
    # filename = input("Filename (.pas): ").lower()
    # if not filename.endswith(".pas"):
    #    filename = filename + ".pas"
    filename = "hello2.pas"
    origin = read_pascal(filename)
    main(origin)

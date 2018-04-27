from parser import Parser
from binaryop import BinaryOp
from symboltable import SymbolTable

def read_pascal(f):
    with open(f, 'r') as ff:
        return ff.read().rstrip("\n")

def main(origin):
    st = SymbolTable()
    Parser.set_origin(origin.lower())
    parse = Parser.parse()
    result = parse.eval(st)

if __name__ == "__main__":
    origin = read_pascal("hello.pas")


    main(origin)
from parser import Parser
from binaryop import BinaryOp

def read_pascal(f):
    with open(f, 'r') as ff:
        return ff.readline().rstrip("\n")

def main(origin):
    Parser.set_origin(origin)
    parse = Parser.parse()
    result = parse.eval()
    return result

if __name__ == "__main__":
    origin = read_pascal("hello.pas")


    print(main(origin))
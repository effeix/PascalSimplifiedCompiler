from parser import Parser

def read_pascal(f):
    with open(f, 'r') as ff:
        return ff.readline().rstrip("\n")

def main(origin):
    Parser.set_origin(origin)
    result = Parser.parse()
    return result

if __name__ == "__main__":
    origin = read_pascal("hello.pas")
    print(main(origin))
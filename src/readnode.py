from node import Node
from intval import IntVal


class ReadNode(Node):
    def eval(self, st):
        var = input("Read: ")
        value = IntVal(int(var)).eval(st)
        return value

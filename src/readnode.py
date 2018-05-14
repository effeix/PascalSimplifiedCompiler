from node import Node
from binaryop import BinaryOp

class ReadNode(Node):
    def eval(self, st):
        var = input()
        value = BinaryOp(int(var)).eval(st)
        return value
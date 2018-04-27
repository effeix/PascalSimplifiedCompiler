from node import Node

class PrintNode(Node):
    def eval(self, st):
        result = self.children[0].eval(st)
        print(result)
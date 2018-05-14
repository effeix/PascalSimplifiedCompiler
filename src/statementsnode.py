from node import Node

class StatementsNode(Node):
    def eval(self, st):
        for child in self.children:
            child.eval(st)

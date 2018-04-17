from node import Node

class StmtsOp(Node):
    def eval(self, st):
        for child in self.children:
            child.eval(st)

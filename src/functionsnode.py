from node import Node


class FunctionsNode(Node):
    def eval(self, st):
        for child in self.children:
            child.eval(st)

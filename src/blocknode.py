from node import Node


class Block(Node):
    def eval(self, st):
        for child in self.children:
            child.eval(st)
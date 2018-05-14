from node import Node

class LoopNode(Node):
    def eval(self, st):
        while self.children[0].eval(st) == True:
            self.children[1].eval(st)

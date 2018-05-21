from node import Node


class Program(Node):
    def eval(self, st):
        self.children[0].eval(st)

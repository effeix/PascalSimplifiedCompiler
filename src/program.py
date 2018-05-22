from node import Node
from symboltable import SymbolTable


class Program(Node):
    def eval(self):
        self.children[0].eval(SymbolTable(None))

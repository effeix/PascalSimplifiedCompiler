from node import Node

class UnaryOp(Node):
    def eval(self):
        if self.children:
            result = self.children[0].eval()
        
        if self.value == "PLUS":
            return result
        
        elif self.value == "MINUS":
            return -result
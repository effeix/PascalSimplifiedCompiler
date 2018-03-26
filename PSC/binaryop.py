from node import Node

class BinaryOp(Node):
    def eval(self):
        if self.children:
            result_a = self.children[0].eval()
            result_b = self.children[1].eval()  

        if self.value == "PLUS":
            return result_a + result_b

        elif self.value == "MINUS":
            return result_a - result_b

        elif self.value == "MULT":
            return result_a * result_b

        elif self.value == "DIV":
            return result_a // result_b
        
        else:
            return self.value




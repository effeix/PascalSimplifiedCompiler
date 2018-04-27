from node import Node

class BinaryOp(Node):
    def eval(self, st):
        if self.children:
            result_a = self.children[0].eval(st)
            result_b = self.children[1].eval(st)  

        if self.value == "PLUS":
            return result_a + result_b

        elif self.value == "MINUS":
            return result_a - result_b

        elif self.value == "MULT":
            return result_a * result_b

        elif self.value == "DIV":
            return result_a // result_b
        
        elif self.value == "AND":
            return result_a and result_b
        
        elif self.value == "OR":
            return result_a or result_b
        
        elif self.value == "MORE_THAN":
            return result_a > result_b
        
        elif self.value == "LESS_THAN":
            return result_a < result_b

        elif self.value == "EQUAL":
            return result_a == result_b

        else:
            return self.value
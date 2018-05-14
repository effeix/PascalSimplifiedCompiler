from node import Node

class BinaryOp(Node):

    def _sametype(self, a, b):
        return (isinstance(a, bool) and isinstance(b, bool)) \
            or (isinstance(a, int) and isinstance(b, int))

    def eval(self, st):

        if self.children:
            a = self.children[0].eval(st)
            b = self.children[1].eval(st)

        if self.value == "PLUS":
            if type(a) != type(b) or (isinstance(a, bool) and isinstance(b, bool)):
                raise ValueError("Variables must be of same type and/or bool not allowed")
            return a + b

        elif self.value == "MINUS":
            if type(a) != type(b) or (isinstance(a, bool) and isinstance(b, bool)):
                raise ValueError("Variables must be of same type and/or bool not allowed") 
              
            return a - b

        elif self.value == "MULT":
            if type(a) != type(b) or (isinstance(a, bool) and isinstance(b, bool)):
                raise ValueError("Variables must be of same type and/or bool not allowed") 
            return a * b

        elif self.value == "DIV":
            if type(a) != type(b) or (isinstance(a, bool) and isinstance(b, bool)):
                raise ValueError("Variables must be of same type and/or bool not allowed")  
            return a // b

        elif self.value == "AND":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type") 
            return a and b

        elif self.value == "OR":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type") 
            return a or b

        elif self.value == "MORE_THAN":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type") 
            return a > b

        elif self.value == "LESS_THAN":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type") 
            return a < b

        elif self.value == "EQUAL":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type") 
            return a == b

        else:
            return self.value

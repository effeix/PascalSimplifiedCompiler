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
            print(a)
            print(isinstance(a, int))
            if not self._sametype(a, b):
                raise ValueError("Variables must be of same type")
            if isinstance(a, int):
                return a + b
            elif isinstance(a, bool):
                return bool(a + b)

        elif self.value == "MINUS":
            return a - b

        elif self.value == "MULT":
            return a * b

        elif self.value == "DIV":
            return a // b

        elif self.value == "AND":
            return a and b

        elif self.value == "OR":
            return a or b

        elif self.value == "MORE_THAN":
            return a > b

        elif self.value == "LESS_THAN":
            return a < b

        elif self.value == "EQUAL":
            return a == b

        elif self.value == "TRUE":
            return True

        elif self.value == "FALSE":
            return False

        else:
            return self.value

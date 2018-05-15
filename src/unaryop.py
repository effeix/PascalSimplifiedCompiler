from node import Node


class UnaryOp(Node):
    def eval(self, st):
        if self.children:
            result = self.children[0].eval(st)

        if self.value == "PLUS":
            if not isinstance(result, bool):
                return result

            raise ValueError("Incompatible types: got \"Boolean\" expected \"Integer\"")

        elif self.value == "MINUS":
            if not isinstance(result, bool):
                return -result

            raise ValueError("Incompatible types: got \"Boolean\" expected \"Integer\"")

        elif self.value == "NOT":
            if isinstance(result, bool):
                return not result
            else:
                return ~result

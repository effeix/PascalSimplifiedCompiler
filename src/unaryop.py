from node import Node
from assembly import Assembly


class UnaryOp(Node):
    def eval(self, st):
        if self.children:
            result = self.children[0].eval(st)

        if self.value == "PLUS":
            if not isinstance(result, bool):
                return result

            raise ValueError("Incompatible types: got \"Boolean\" expected \"Integer\"")

        elif self.value == "MINUS":
            Assembly.append("""  NEG EBX""")

            if not isinstance(result, bool):
                return -result

            raise ValueError("Incompatible types: got \"Boolean\" expected \"Integer\"")

        elif self.value == "NOT":
            Assembly.append("""  NOT EBX""")

            if isinstance(result, bool):
                return not result
            else:
                return ~result

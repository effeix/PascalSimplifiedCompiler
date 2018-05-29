from node import Node
from assembly import Assembly, LOGIC_OPS, ARITHMETIC_OPS, JUMP_OPS, STACK_OPS


class BinaryOp(Node):
    def eval(self, st, n_id=None):

        a = self.children[0].eval(st)
        self.__generate_assembly("PUSH")

        b = self.children[1].eval(st)
        self.__generate_assembly("POP")

        if self.value == "PLUS":
            if type(a) != type(b):
                raise ValueError("Variables must be of same type")
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("ADD")
            return a + b

        elif self.value == "MINUS":
            if type(a) != type(b):
                raise ValueError("Variables must be of same type")
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("SUB")
            return a - b

        elif self.value == "MULT":
            if type(a) != type(b):
                raise ValueError("Variables must be of same type")
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("IMUL")
            return a * b

        elif self.value == "DIV":
            if type(a) != type(b):
                raise ValueError("Variables must be of same type")
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("IDIV")
            return a // b

        elif self.value == "AND":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type")
            self.__generate_assembly("AND")
            if isinstance(a, bool) and isinstance(b, bool):
                return a and b
            else:
                return a & b

        elif self.value == "OR":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type")
            self.__generate_assembly("OR")
            if isinstance(a, bool) and isinstance(b, bool):
                return a or b
            else:
                return a | b

        elif self.value == "MORE_THAN":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type")
            self.__generate_assembly("JG", n_id=n_id)
            return a > b

        elif self.value == "LESS_THAN":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type")
            self.__generate_assembly("JL", n_id=n_id)
            return a < b

        elif self.value == "EQUAL":
            if(type(a) != type(b)):
                raise ValueError("Variables must be of same type")
            self.__generate_assembly("JE", n_id=n_id)
            return a == b

        else:
            raise ValueError("Unkwown Operation")

    def __generate_assembly(self, op, n_id=""):
        if op in JUMP_OPS:
            commands = [
                """  CMP EAX, EBX""",
                f"""  CALL binop_{op.lower()}""",
                """  CMP EBX, False""",
                f"""  JE EXIT_{n_id}"""
            ]

        elif op in ARITHMETIC_OPS or op in LOGIC_OPS:
            if op == "IMUL" or op == "IDIV":
                if op == "IDIV":
                    Assembly.append("""  MOV EDX, 0""")
                commands = [
                    f"""  {op} EBX""",
                    """  MOV EBX, EAX"""
                ]
            elif op == "SUB":
                commands = [
                    f"""  {op} EAX, EBX""",
                    """  MOV EBX, EAX"""
                ]
            else:
                commands = f"""  {op} EBX, EAX"""

        elif op in STACK_OPS:
            if op == "PUSH":
                register = "EBX"
            elif op == "POP":
                register = "EAX"

            commands = f"""  {op} {register}"""

        Assembly.append(commands)

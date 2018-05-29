from node import Node
from assembly import Assembly, LOGIC_OPS, ARITHMETIC_OPS, JUMP_OPS, STACK_OPS


class BinaryOp(Node):
    def eval(self, st, n_id=None):

        a = self.children[0].eval(st)
        self.__generate_assembly("PUSH")

        b = self.children[1].eval(st)
        self.__generate_assembly("POP")

        if type(a) != type(b):
            raise ValueError("Variables must be of same type")

        if self.value == "PLUS":
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("ADD")
            return a + b

        elif self.value == "MINUS":
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("SUB")
            return a - b

        elif self.value == "MULT":
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("IMUL")
            return a * b

        elif self.value == "DIV":
            if isinstance(a, bool) and isinstance(b, bool):
                raise ValueError("This operation does not support bool")
            self.__generate_assembly("IDIV")
            return a // b

        elif self.value == "AND":
            self.__generate_assembly("AND")
            if isinstance(a, bool) and isinstance(b, bool):
                return a and b
            else:
                return a & b

        elif self.value == "OR":
            self.__generate_assembly("OR")
            if isinstance(a, bool) and isinstance(b, bool):
                return a or b
            else:
                return a | b

        elif self.value == "MORE_THAN":
            self.__generate_assembly("JG", n_id=n_id)
            return a > b

        elif self.value == "LESS_THAN":
            self.__generate_assembly("JL", n_id=n_id)
            return a < b

        elif self.value == "EQUAL":
            self.__generate_assembly("JE", n_id=n_id)
            return a == b

        else:
            raise ValueError("Unkwown Operation")

    def __generate_assembly(self, instruction, n_id=""):
        if instruction in JUMP_OPS:
            commands = [
                """  CMP EAX, EBX""",
                f"""  CALL binop_{instruction.lower()}""",
                """  CMP EBX, False""",
                f"""  JE EXIT_{n_id}"""
            ]

        elif instruction in ARITHMETIC_OPS + LOGIC_OPS:
            if instruction == "IMUL" or instruction == "IDIV":
                if instruction == "IDIV":
                    Assembly.append("""  MOV EDX, 0""")
                commands = [
                    f"""  {instruction} EBX""",
                    """  MOV EBX, EAX"""
                ]
            elif instruction == "SUB":
                commands = [
                    f"""  {instruction} EAX, EBX""",
                    """  MOV EBX, EAX"""
                ]
            else:
                commands = f"""  {instruction} EBX, EAX"""

        elif instruction in STACK_OPS:
            if instruction == "PUSH":
                register = "EBX"
            elif instruction == "POP":
                register = "EAX"

            commands = f"""  {instruction} {register}"""

        Assembly.append(commands)

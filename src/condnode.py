from node import Node
from assembly import Assembly


class CondNode(Node):
    def eval(self, st):

        condition = self.children[0]
        true_stmts = self.children[1]
        false_stmts = self.children[2]

        if Assembly.get_exec_type() == "i":
            if condition.eval(st, n_id=self.identifier):
                true_stmts.eval(st)
            else:
                false_stmts.eval(st)

        else:
            condition.eval(st, n_id=self.identifier)
            true_stmts.eval(st)
            self.__generate_assembly("BEFORE_ELSE", n_id=self.identifier)
            false_stmts.eval(st)
            self.__generate_assembly("AFTER_ELSE", n_id=self.identifier)

    def __generate_assembly(self, instruction, n_id=""):
        if instruction == "BEFORE_ELSE":
            commands = [
                f"""  JMP FALSE_{n_id}""",
                f"""  EXIT_{n_id}:"""
            ]
        elif instruction == "AFTER_ELSE":
            commands = f"""  FALSE_{n_id}:"""

        Assembly.append(commands)

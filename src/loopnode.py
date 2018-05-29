from node import Node
from assembly import Assembly


class LoopNode(Node):
    def eval(self, st):

        condition = self.children[0]
        statements = self.children[1]

        self.__generate_assembly("LOOP_ENTER")

        while condition.eval(st, n_id=self.identifier):
            statements.eval(st)

        self.__generate_assembly("LOOP_EXIT")

    def __generate_assembly(self, instruction):
        if instruction == "LOOP_ENTER":
            commands = f"""  WHILE_{self.identifier}:"""

        elif instruction == "LOOP_EXIT":
            commands = [
                f"""  JMP WHILE_{self.identifier}""",
                f"""  EXIT_{self.identifier}:"""
            ]

        Assembly.append(commands)

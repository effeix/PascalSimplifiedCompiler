from node import Node
from assembly import Assembly


class WriteNode(Node):
    def eval(self, st):
        result = self.children[0].eval(st)
        self.__generate_assembly()
        print(result)

    def __generate_assembly(self):
        commands = [
            """  PUSH EBX""",
            """  CALL print"""
        ]

        Assembly.append(commands)
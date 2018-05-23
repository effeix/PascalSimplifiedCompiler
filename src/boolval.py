from node import Node
from assembly import Assembly


class BoolVal(Node):
    def eval(self, st):
        self.__generate_assembly(self.value)
        return self.value

    def __generate_assembly(self, value):
        Assembly.append(f"""  MOV EBX, ${value}""")
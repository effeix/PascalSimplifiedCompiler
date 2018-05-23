from node import Node
from assembly import Assembly


class IdentifierNode(Node):
    def eval(self, st):
        self.__generate_assembly(self.value, st.identifier)
        return st.get_identifier(self.value)

    def __generate_assembly(self, value, st_id):
        Assembly.append(f"""  MOV EBX, [{value}_{st_id}]""")

from node import Node
from assembly import Assembly


class AssignerNode(Node):
    def __init__(self, _vartype=None, _value=None):
        self.value = _value
        self.children = []
        self.vartype = _vartype

    def eval(self, st):
        if self.vartype:
            st.create_identifier(self.value, self.vartype)
        else:
            val = self.children[0].eval(st)
            st.set_identifier(self.value, val)
            if st.is_global:
                self.__generate_assembly(self.value, st.identifier)

    def __generate_assembly(self, value, st_id):
        Assembly.append(f"""  MOV [{value}_{st_id}], EBX""")
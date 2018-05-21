from node import Node
from assembly import Assembly


class VarDecNode(Node):
    def eval(self, st):
        for child in self.children:
            if st.is_global:
                self.generate_assembly(child.value, st.identifier)
            child.eval(st)

    def generate_assembly(self, var_name, st_id):
        Assembly.append(f"""  {var_name}_{st_id} RESD 1""")
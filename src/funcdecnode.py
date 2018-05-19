from node import Node

"""
AST

Node: FuncDecNode
    | Child 0: VarDecNode  (arguments)
    | Child 1: VarDecNode  (local variables)
    | Child 2: FuncDecNode
    | Child 3: StatementsNode
"""
class FuncDecNode(Node):
    def eval(self, st):
        st.create_identifier(self.value, "FUNC")
        st.set_identifier(self.value, self)

    def __repr__(self):
        return f"Function({self.value})"

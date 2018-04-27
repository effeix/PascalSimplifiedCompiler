from node import Node

class IdentifierNode(Node):
    def eval(self, st):
        return st.get_identifier(self.value)

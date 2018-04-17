from node import Node

class WordResOp(Node):
    def eval(self, st):
        return st.get_identifier(self.value)

from node import Node


class FuncDecNode(Node):
    def eval(self, st):
        st.create_identifier(self.value, "FUNC")
        st.set_identifier(self.value, self)

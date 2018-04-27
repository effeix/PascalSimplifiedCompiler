from node import Node

class AssignerNode(Node):
    def eval(self, st):
        word = self.value
        val = self.children[0].eval(st)
        st.set_identifier(word, val)




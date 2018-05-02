from node import Node

class AssignerNode(Node):
    def __init__(self, _vartype=None, _value=None):
        self.value = _value
        self.children = []
        self.vartype = _vartype

    def eval(self, st):
        if not self.vartype:
            val = self.children[0].eval(st)
        
        if self.vartype:
            st.create_identifier(self.value, self.vartype)
        else:
            st.set_identifier(self.value, val)




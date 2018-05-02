from node import Node

class AssignerNode(Node):
    def __init__(self, _vartype=None, _value=None):
        super().__init__(self)
        self.vartype = _vartype

    def eval(self, st):
        varname = self._value
        vartype = self.vartype
        val = self.children[0].eval(st)
        
        if self._vartype:
            st.create_identifier(varname, vartype)
        else:
            st.set_identifier(varname, val)




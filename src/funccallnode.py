from node import Node
from symboltable import SymbolTable


"""
FuncCallNode.children = [VarDecNode, VarDecNode | NullNode, FuncDecNode, StatementsNode]
"""


class FuncCallNode(Node):
    def eval(self, st):
        funcdecnode = st.get_identifier(self.value)
        func_arguments = funcdecnode.children[0]
        local_variables = funcdecnode.children[1].children[0]
        local_functions = funcdecnode.children[1].children[1]
        local_statements = funcdecnode.children[1].children[2]

        local_st = SymbolTable(st)

        func_arguments.eval(local_st)
        local_variables.eval(local_st)
        local_functions.eval(local_st)
        local_statements.eval(local_st)

        ret = local_st.get_identifier(self.value)

        return ret
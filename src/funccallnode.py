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

        name_args = [arg.value for arg in func_arguments.children]
        value_args = [(arg[0].eval(local_st), arg[1]) for arg in self.children[0]]
        new_value_args = []

        for arg in value_args:
            if isinstance(arg[0], int):
                if isinstance(arg[0], bool):
                    new_value_args.append([arg[0], "BOOLEAN"])
                else:
                    new_value_args.append([arg[0], "INTEGER"])

        if not len(func_arguments.children) == len(new_value_args) + 1:
            raise ValueError(f"wrong number of parameters specified for call to {self.value}")

        i = 0
        while i < len(new_value_args):
            if local_st.get_identifier(name_args[i], what=0) != new_value_args[i][1]:
                raise ValueError(f"Incompatible type for arg no. {i+1} in call to {self.value}")

            local_st.set_identifier(name_args[i], new_value_args[i][0])

            i += 1

        local_variables.eval(local_st)
        local_functions.eval(local_st)
        local_statements.eval(local_st)

        ret = local_st.get_identifier(self.value)

        return ret

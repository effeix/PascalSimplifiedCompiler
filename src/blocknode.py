from node import Node
from statementsnode import StatementsNode
from assembly import Assembly, CONSTANTS, DATA_SEGMENT, BSS_SEGMENT, \
    PRINT_PROC, IF_WHILE_PROC, START, INTERRUPT


class Block(Node):
    def eval(self, st):
        self.__assembly_init()

        for child in self.children:
            if isinstance(child, StatementsNode):
                self.__assembly_procs()

            child.eval(st)

        self.__assembly_terminate()

    def __assembly_init(self):

        Assembly.append(CONSTANTS)
        Assembly.append(DATA_SEGMENT)
        Assembly.append(BSS_SEGMENT)

    def __assembly_procs(self):
        Assembly.append(PRINT_PROC)
        Assembly.append(IF_WHILE_PROC)
        Assembly.append(START)

    def __assembly_terminate(self):

        Assembly.append(INTERRUPT)
class SymbolTable():
    def __init__(self):
        self.table = {}

    def get_identifier(self, id):
        if not id in self.table.keys():
            raise KeyError(f'{id} not in SymbolTable')
        
        return self.table[id]

    def set_identifier(self, id, value):        
        self.table[id] = value
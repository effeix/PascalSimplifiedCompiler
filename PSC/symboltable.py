class SymbolTable():
    def __init__(self):
        self.table = {}

    def get_identifier(self, _id):
        if not _id in self.table.keys():
            raise KeyError(f'{_id} not in SymbolTable')
        
        return self.table[_id][0]

    def create_identifier(self, _id, _type):
    	if _id not in self.table:
    		self.table[_id] = [_type]
    	else:
    		raise KeyError(f"Variable already exists: {_id}")

    def set_identifier(self, _id, _value):        
        if _id in self.table:
        	self.table[_id].append(_value)
        else:
        	raise KeyError(f"Variable is not defined: {_id}")
class SymbolTable():
    def __init__(self):
        self.table = {}

    def get_identifier(self, idx):
        if idx not in self.table.keys():
            raise KeyError(f'{idx} not in SymbolTable')

        return self.table[idx][1]

    def create_identifier(self, idx, _type):
        if idx not in self.table:
            self.table[idx] = [_type, None]
        else:
            raise KeyError(f"Variable already exists: {idx}")

    def set_identifier(self, idx, _value):
        if idx in self.table:
            if (self.table[idx][0] == "BOOLEAN" and isinstance(_value, bool)) \
                    or (self.table[idx][0] == "INTEGER"
                        and type(_value) != type(True)
                        and isinstance(_value, int)):
                self.table[idx][1] = _value
            else:
                raise KeyError(
                    "Variable type and assignment type does"
                    + " not match")

        else:
            raise KeyError(f"Variable is not defined: {idx}")
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
            if self._trueboolean(idx, _value) \
                or self._trueint(idx, _value) \
                    or self._truefunc(idx):
                self.table[idx][1] = _value
            else:
                raise KeyError(
                    "Variable type and assignment type does"
                    + " not match")

        else:
            raise KeyError(f"Variable is not defined: {idx}")

    def _trueboolean(self, idx, value):
        return self.table[idx][0] == "BOOLEAN" and isinstance(value, bool)

    def _trueint(self, idx, value):
        return self.table[idx][0] == "INTEGER" \
            and isinstance(value, int) \
            and not isinstance(value, bool)

    def _truefunc(self, idx):
        return self.table[idx][0] == "FUNC"
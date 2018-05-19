class SymbolTable():
    def __init__(self, parent):
        self.table = {}
        self.parent = parent
        self.is_global = False

        if parent is None:
            self.is_global = True

    def get_identifier(self, idx):
        if idx not in self.table.keys():
            if not self.is_global:
                identifier = self.parent.get_identifier(idx)
                return identifier
            else:
                raise NameError(f'Error: Identifier not found "{idx}"')
        else:
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
                raise NameError('Error: Incompatible types')

        else:
            if not self.is_global:
                self.parent.set_identifier(idx, _value)
            else:
                raise NameError(f'Error: Identifier not found "{idx}"')

    def _trueboolean(self, idx, value):
        return self.table[idx][0] == "BOOLEAN" and isinstance(value, bool)

    def _trueint(self, idx, value):
        return self.table[idx][0] == "INTEGER" \
            and isinstance(value, int) \
            and not isinstance(value, bool)

    def _truefunc(self, idx):
        return self.table[idx][0] == "FUNC"

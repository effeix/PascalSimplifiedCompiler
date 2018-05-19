from string import ascii_letters, digits
from token import Token

RESERVED = {
    "and": "AND",
    "begin": "BEGIN",
    "boolean": "BOOLEAN",
    "do": "DO",
    "else": "ELSE",
    "end": "END",
    "function": "FUNCTION",
    "if": "IF",
    "integer": "INTEGER",
    "not": "NOT",
    "or": "OR",
    "write": "WRITE",
    "program": "PROGRAM",
    "read": "READ",
    "then": "THEN",
    "var": "VAR",
    "while": "WHILE"
}

SINGLE_CHAR = {
    "(": "OPEN_PAR",
    ")": "CLOSE_PAR",
    "*": "MULT",
    "+": "PLUS",
    ",": "COMMA",
    "-": "MINUS",
    ".": "DOT",
    "/": "DIV",
    ";": "SEMICOLON",
    "<": "LESS_THAN",
    ">": "MORE_THAN",
    "=": "EQUAL"
}

ALLOWED_VARNAME_CHARS = ascii_letters + digits + "_"


class Tokenizer():

    def __init__(self):
        self.origin = "0"
        self.position = 0
        self.line_number = 0
        self.current = None

    def _isnumber(self, token):
        return token.isdigit()

    def _isalpha(self, token):
        return token.isalpha()

    def _isalphanum(self, token):
        return token.isalnum()

    def _ignore_extras(self):
        is_dirty = True
        while is_dirty:
            if self.position < len(self.origin):

                if self.origin[self.position] == " ":
                    self.position += 1

                elif self.origin[self.position] == "\n":
                    self.position+=1
                    self.line_number += 1

                elif self.origin[self.position] == "{":
                    while self.origin[self.position] != "}":
                        if self.position < len(self.origin)-1:
                            self.position += 1

                        else:
                            raise ValueError("Invalid token")
                    self.position += 1

                else:
                    is_dirty = False
            else:
                is_dirty = False

    def next(self):
        self.current = None
        aux = ""

        self._ignore_extras()

        if self.position < len(self.origin):

            if self.origin[self.position] in SINGLE_CHAR:
                self.current = Token(SINGLE_CHAR[self.origin[self.position]])
                self.position += 1

            elif self.origin[self.position] == ":":
                if self.origin[self.position+1] == "=":
                    self.current = Token("ASSIGN")
                    self.position += 2
                else:
                    self.current = Token("COLON")
                    self.position += 1

            elif self._isnumber(self.origin[self.position]):
                while self._isnumber(self.origin[self.position]):

                    aux += self.origin[self.position]

                    self.position += 1

                    if self.position >= len(self.origin)-1:
                        break

                self.current = Token("INT", int(aux))
                aux = ""

            elif self._isalpha(self.origin[self.position]):
                while self.origin[self.position] in ALLOWED_VARNAME_CHARS:

                    aux += self.origin[self.position]

                    self.position += 1

                    if self.position >= len(self.origin)-1:
                        break

                if aux == "true":
                    self.current = Token("BOOL", True)

                elif aux == "false":
                    self.current = Token("BOOL", False)

                elif aux in RESERVED:
                    self.current = Token(RESERVED[aux])

                else:
                    self.current = Token("IDENTIFIER", aux)

                aux = ""

            else:
                raise ValueError(f"invalid token {self.origin[self.position]}")

from token import Token

RESERVED = {
    "program": "PROGRAM",
    "begin": "BEGIN",
    "end": "END",
    "print": "PRINT",
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "and": "AND",
    "or": "OR",
    "while": "WHILE",
    "do": "DO",
    "var": "VAR",
    "bool": "BOOL",
    "int": "INTEGER"
}

SINGLE_CHAR = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULT",
    "/": "DIV",
    "&": "AND",
    "|": "OR",
    "(": "OPEN_PAR",
    ")": "CLOSE_PAR",
    ";": "STMT_FINISH",
    ".": "DOT",
    "<": "LESS_THAN",
    ">": "MORE_THAN",
    ",": "COMMA",
}

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
                while self._isalpha(self.origin[self.position]) or self.origin[self.position] == "_":
                    
                    aux += self.origin[self.position]

                    self.position += 1

                    if self.position >= len(self.origin)-1:
                        break
                
                if aux in RESERVED:
                    self.current = Token(RESERVED[aux])

                else:
                    self.current = Token("WORD", aux)
                
                aux = ""

            else:
                raise ValueError("String {} is an invalid token".format(self.origin[self.position]))


from token2 import Token

class Tokenizer():

    def __init__(self):
        self.origin = "0"
        self.position = 0
        self.reserved_words = ["BEGIN", "END", "Print", ":="]
        self.current = None

    def isnumber(self, token):
        return token.isdigit()

    def next(self):
        self.current = None
        aux = ""

        #checks for commentary blocks and white spaces in no particular order, and ignores them
        while True:
            if self.position < len(self.origin):
                if self.origin[self.position] == " ":
                    while self.origin[self.position] == " ":
                        if self.position < len(self.origin)-1:
                            self.position += 1
                                
                        else:
                            self.position += 1
                            break
            
                elif self.origin[self.position] == "{":
                    while self.origin[self.position] != "}":
                        if self.position < len(self.origin)-1:
                            self.position += 1
                            
                        else:
                            raise ValueError("Invalid token")
                    self.position += 1
                
                elif self.origin[self.position] == "\n":
                    self.position+=1
            
                else:
                    break
            
            else:
                break
        
        #check if its a valid token
        if self.position < len(self.origin):
            if self.origin[self.position] == "+":
                self.current = Token("PLUS", None)
                self.position += 1
            
            elif self.origin[self.position] == "-":
                self.current = Token("MINUS", None)
                self.position += 1
            
            elif self.origin[self.position] == "*":
                self.current = Token("MULT", None)
                self.position += 1
            
            elif self.origin[self.position] == "/":
                self.current = Token("DIV", None)
                self.position += 1 
            
            elif self.origin[self.position] == "(":
                self.current = Token("OPEN_PAR", None)
                self.position += 1 
            
            elif self.origin[self.position] == ")":
                self.current = Token("CLOSE_PAR", None)
                self.position += 1
            
            elif self.origin[self.position] == ";":
                self.current = Token("STMT_FINISH", None)
                self.position += 1

            elif self.origin[self.position] == ".":
                self.current = Token("DOT")
                self.position += 1
            
            elif self.origin[self.position] == ":":
                if self.origin[self.position+1] == "=":
                    self.current = Token("ASSIGN", None)
                    self.position += 2
                else:
                    ValueError("Invalid token")

            elif self.isnumber(self.origin[self.position]):
                while self.isnumber(self.origin[self.position]):
                    aux += self.origin[self.position]
                    
                    if self.position < len(self.origin)-1:
                        self.position += 1
                    
                    else:
                        self.position += 1
                        break
                
                self.current = Token("INT", int(aux))
                aux = ""
            
            elif self.isalpha(self.origin[self.position]):
                while self.isalpha(self.origin[self.position]) or self.origin[self.position] == "_":
                    aux += self.origin[self.position]

                    if self.position < len(self.origin)-1:
                        self.position += 1
                    
                    else:
                        self.position += 1
                        break
                
                if aux == "BEGIN":
                    self.current = Token("BEGIN", None)
                elif aux == "END":
                    self.current = Token("END", None)
                elif aux == "Print":
                    self.current = Token("Print", None)
                elif aux == "PROGRAM":
                    self.current = Token("PROGRAM")
                else:
                    self.current = Token("IDENTIFIER", aux)
                aux = ""

            else:
                raise ValueError("Invalid token")
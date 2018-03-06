from token import Token

class Tokenizer():

    def __init__(self):
        self.origin = "0"
        self.position = 0
        self.current = None

    def isnumber(self, token):
        return token.isdigit()

    def next(self):
        self.current = None
        aux = ""

        if self.position < len(self.origin):
            while self.origin[self.position] == " ":
                if self.position < len(self.origin)-1:
                    self.position += 1
                        
                else:
                    self.position += 1
                    break
        
        if self.position < len(self.origin):
            if self.origin[self.position] == "{":
                while self.origin[self.position] != "}":
                    if self.position < len(self.origin)-1:
                        self.position += 1
                        
                    else:
                        raise ValueError("Invalid token")
                self.position += 1
        
        if self.position < len(self.origin):
            while self.origin[self.position] == " ":
                if self.position < len(self.origin)-1:
                    self.position += 1
                        
                else:
                    self.position += 1
                    break

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

            else:
                raise ValueError("Invalid token")
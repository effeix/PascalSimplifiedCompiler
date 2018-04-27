from token import Token

class Tokenizer():

    def __init__(self):
        self.origin = "0"
        self.position = 0
        self.res_words = {
            "program":"PROGRAM",
            "begin":"BEGIN",
            "end":"END",
            "print":"PRINT",
            "if":"IF",
            "then":"THEN",
            "else":"ELSE",
            "and":"AND",
            "or":"OR",
            "while":"WHILE",
            "do":"DO",
        }
        self.single_char_tokens = {
            "+":"PLUS",
            "-":"MINUS",
            "*":"MULT",
            "/":"DIV",
            "&":"AND",
            "|":"OR",
            "(":"OPEN_PAR",
            ")":"CLOSE_PAR",
            ";":"STMT_FINISH",
            ".":"DOT",
            "<":"LESS_THAN",
            ">":"MORE_THAN",
        }
        self.current = None

    def isnumber(self, token):
        return token.isdigit()
    
    def isalphas(self, token):
        return token.isalpha()
    
    def pre_processing(self):
        is_dirty = True
        while is_dirty:
            if self.position < len(self.origin):
                
                if self.origin[self.position] == " ":
                    self.position += 1
                
                elif self.origin[self.position] == "\n":
                    self.position+=1
                
                elif self.origin[self.position] == "{":
                    while self.origin[self.position] != "}":
                        if self.position < len(self.origin)-1:
                            self.position += 1
                            
                        else:
                            raise ValueError("Invalid token")
                    self.position += 1

                else:
                    is_dirty = False

    def next(self):
        self.current = None
        aux = ""

        self.pre_processing()
        
        if self.position < len(self.origin):
            
            if self.origin[self.position] in self.single_char_tokens:
                self.current = Token(self.single_char_tokens[self.origin[self.position]])
                self.position += 1
            
            
            elif self.origin[self.position] == ":":
                if self.origin[self.position+1] == "=":
                    self.current = Token("ASSIGN")
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
            
            elif self.isalphas(self.origin[self.position]):
                while self.isalphas(self.origin[self.position]) or self.origin[self.position] == "_":
                    aux += self.origin[self.position]

                    if self.position < len(self.origin)-1:
                        self.position += 1
                    
                    else:
                        self.position += 1
                        break
                
                if aux in self.res_words:
                    self.current = Token(self.res_words[aux])

                else:
                    self.current = Token("WORD", aux)
                
                aux = ""

            else:
                raise ValueError("String {} is an invalid token".format(self.origin[self.position]))
from token import Token

class Tokenizer():

    def __init__(self):
        self.origin = "0"
        self.position = -1
        self.current = None
        self.ops = ['+','-']

    def isop(self, token):
        return token in self.ops

    def isnumber(self, token):
        return token.isdigit()

    def isspace(self, token):
        return token == " "

    def next(self):
        """Update token being analyzed"""

        aux = ""
        self.position += 1

        if self.position >= len(self.origin):
            self.current = None

        elif self.isop(self.origin[self.position]):
            if self.origin[self.position] == "+":
                self.current = Token("PLUS")
            elif self.origin[self.position] == "-":
                self.current = Token("MINUS")

        elif self.isnumber(self.origin[self.position]):
            while self.isnumber(self.origin[self.position]):
                aux += self.origin[self.position]

                if self.position + 1 <= len(self.origin):
                    if self.isnumber(self.origin[self.position+1]):
                        self.position += 1
                    else:
                        break
                else:
                    break

                if self.position >= len(self.origin):
                    self.current = None
                    break

            self.current = Token("INT", int(aux))

        else:
            if self.isspace(self.origin[self.position]):
                self.position += 1
            else:
                raise ValueError("Invalid token")
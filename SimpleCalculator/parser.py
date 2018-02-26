class Parser():

    ERROR = "Invalid token"
    tokens = Tokenizer()
    
    def parse():
        result = 0
        token = Parser.tokens.next()

        if token.type == "INT":
            result = token
            token = Parser.tokens.next()
            
            while token:
                if token.type == "PLUS":
                    token = Parser.tokens.next()
                    if is_int(token):
                        result += token
                    else:
                        raise ValueError(ERROR)
                elif token.type == "MINUS":
                    token = Parser.tokens.next()
                    if is_int(token):
                        result -= token
                    else:
                        raise ValueError(ERROR)
                else:
                    raise ValueError(ERROR)
        else:
            raise ValueError(ERROR)
            
        return result
                    



        
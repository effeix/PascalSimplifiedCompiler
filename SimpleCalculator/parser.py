class Parser():

    ERROR = "Invalid token"
    tokens = Tokenizer()
    
    def parse():
        result = 0
        Parser.tokens.next()

        if Parser.tokens.current.type == "INT":
            result = Parser.tokens.current.value
            Parser.tokens.next()
            
            while Parser.tokens.current.type != None:
                if Parser.tokens.current.type == "PLUS":
                    Parser.tokens.next()
                    if Parser.tokens.current.type == "INT":
                        result += Parser.tokens.current.value
                    else:
                        raise ValueError(ERROR)
                elif Parser.tokens.current.type == "MINUS":
                    Parser.tokens.next()
                    if Parser.tokens.current.type == "INT":
                        result -= Parser.tokens.current.value
                    else:
                        raise ValueError(ERROR)
                else:
                    raise ValueError(ERROR)

                Parser.tokens.next()
        else:
            raise ValueError(ERROR)
            
        return result

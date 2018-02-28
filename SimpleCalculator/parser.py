from tokenizer import Tokenizer

class Parser():

    ERROR = "Invalid token"
    tokens = Tokenizer()
    
    def parse():
        result = 0
        Parser.tokens.next()

        print(Parser.tokens.current.value)

        if Parser.tokens.current.type == "INT":
            result = Parser.tokens.current.value
            Parser.tokens.next()

            print(Parser.tokens.current.value)
            
            while Parser.tokens.current.type != None:
                if Parser.tokens.current.type == "PLUS":
                    Parser.tokens.next()
                    if Parser.tokens.current.type == "INT":
                        result += Parser.tokens.current.value
                    else:
                        raise ValueError(Parser.ERROR)
                elif Parser.tokens.current.type == "MINUS":
                    Parser.tokens.next()
                    if Parser.tokens.current.type == "INT":
                        result -= Parser.tokens.current.value
                    else:
                        raise ValueError(Parser.ERROR)
                else:
                    raise ValueError(Parser.ERROR)

                Parser.tokens.next()
        else:
            raise ValueError(Parser.ERROR)
            
        return result

from tokenizer import Tokenizer

class Parser():
    ERROR = "Invalid token"
    tokens = Tokenizer()

    def parse_term():
        result = 0
        Parser.tokens.next()


        if Parser.tokens.current.type == "INT":
            result = Parser.tokens.current.value  
            Parser.tokens.next()
            
            while Parser.tokens.current != None:
                if Parser.tokens.current.type == "MULT":
                    Parser.tokens.next()
                    
                    if Parser.tokens.current.type == "INT":
                        result *= Parser.tokens.current.value
                    
                    else:
                        raise ValueError(Parser.ERROR)
                
                elif Parser.tokens.current.type == "DIV":
                    Parser.tokens.next()
                    
                    if Parser.tokens.current.type == "INT":
                        result //= Parser.tokens.current.value
                    
                    else:
                        raise ValueError(Parser.ERROR)
                
                else:
                    raise ValueError(Parser.ERROR)

                Parser.tokens.next()
        
        else:
            raise ValueError(Parser.ERROR)
            
        return result

    
    def parse_expression():
        result = 0
        Parser.tokens.next()

        result = parse_term()
        
        Parser.tokens.next()
        
        while Parser.tokens.current != None:
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
            
        return result
    
    
from tokenizer import Tokenizer

class Parser():
    ERROR = "Invalid token"
    tokens = Tokenizer()

    def parse_term():
        result = 0

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
                
                elif Parser.tokens.current.type == "PLUS":
                    break
                
                elif Parser.tokens.current.type == "MINUS":
                    break
                
                else:
                    raise ValueError(Parser.ERROR)



                Parser.tokens.next()
        
        else:
            raise ValueError(Parser.ERROR)
            
        return result
    
    def parse_expression():
        result = 0
        Parser.tokens.next()     

        result = Parser.parse_term()
        
        while Parser.tokens.current != None:
            if Parser.tokens.current.type == "PLUS":
                Parser.tokens.next()
                
                result_term = Parser.parse_term()
                result += result_term        
            
            elif Parser.tokens.current.type == "MINUS":
                Parser.tokens.next()
                
                result_term = Parser.parse_term()
                result -= result_term
            
            
            
        return result
    
    
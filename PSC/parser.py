from tokenizer import Tokenizer

class Parser():
    ERROR = "Invalid token"

    term_ops = ["MULT", "DIV"]
    expression_ops = ["MINUS", "PLUS"]

    tokens = Tokenizer()

    def set_origin(origin):
        Parser.tokens.origin = origin 

    def parse():
        Parser.tokens.next()
        return Parser.parse_expression()

    def parse_factor():
        result = 0

        if Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()
            expr = Parser.parse_expression()

            if Parser.tokens.current == None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)
            
            Parser.tokens.next()
            return expr

        if Parser.tokens.current.type == "INT":
            result = Parser.tokens.current.value
            Parser.tokens.next()

        else:
            raise ValueError(Parser.ERROR)
        
        return result

    def parse_term():
        result = 0

        result = Parser.parse_factor()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.term_ops:
            if Parser.tokens.current.type == "MULT":
                Parser.tokens.next()
                
                result_factor = Parser.parse_factor()
                result *= result_factor
                
            elif Parser.tokens.current.type == "DIV":
                Parser.tokens.next()
                
                result_factor = Parser.parse_factor()
                result //= result_factor
            
            Parser.tokens.next()
           
        return result
    
    def parse_expression():
        result = 0     

        result = Parser.parse_term()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.expression_ops:
            if Parser.tokens.current.type == "PLUS":
                Parser.tokens.next()
                
                result_term = Parser.parse_term()
                result += result_term        
            
            elif Parser.tokens.current.type == "MINUS":
                Parser.tokens.next()
                
                result_term = Parser.parse_term()
                result -= result_term          
            
        return result 
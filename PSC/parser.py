from tokenizer import Tokenizer
from binaryop import BinaryOp
from unaryop import UnaryOp

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

        if Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()
            expr = Parser.parse_expression()

            if Parser.tokens.current == None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)
            
            Parser.tokens.next()
            return expr

        if Parser.tokens.current.type == "INT":
            result_node = BinaryOp(Parser.tokens.current.value)
            Parser.tokens.next()
            return result_node

        else:
            raise ValueError(Parser.ERROR)          

    def parse_term():
        result = Parser.parse_factor()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.term_ops:
            result_cp = result
            
            result = BinaryOp(Parser.tokens.current.type)
            
            Parser.tokens.next()
                
            result_factor = Parser.parse_factor()
 
            result.set_child(result_cp)
            result.set_child(result_factor)

            Parser.tokens.next()

        return result
    
    def parse_expression():
        result = Parser.parse_term()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.expression_ops:
            result_cp = result
            
            result = BinaryOp(Parser.tokens.current.type)
            
            Parser.tokens.next()
                
            result_term = Parser.parse_term()
            
            result.set_child(result_cp)
            result.set_child(result_term)       
            
        return result
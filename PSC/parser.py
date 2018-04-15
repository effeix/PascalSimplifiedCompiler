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
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)  

        elif Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()
            expr = Parser.parse_expression()

            if Parser.tokens.current == None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)
            
            Parser.tokens.next()
            return expr

        elif Parser.tokens.current.type == "INT":
            result = BinaryOp(Parser.tokens.current.value)
            
            Parser.tokens.next()
            return result

        elif Parser.tokens.current.type in Parser.expression_ops:
            result = UnaryOp(Parser.tokens.current.type)

            Parser.tokens.next()
            result.set_child(Parser.parse_factor())

            return result

        else:
            raise ValueError(Parser.ERROR)          

    def parse_term():
        result = Parser.parse_factor()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.term_ops:
            result_cp = result
            
            result = BinaryOp(Parser.tokens.current.type)
            
            Parser.tokens.next()

            result.set_child(result_cp)
            result.set_child(Parser.parse_factor())

        return result
    
    def parse_expression():
        result = Parser.parse_term()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.expression_ops:
            result_cp = result
            
            result = BinaryOp(Parser.tokens.current.type)
            
            Parser.tokens.next()
            
            result.set_child(result_cp)
            result.set_child(Parser.parse_term())
        
        #se eu to acabando a conta n tem um close parents e tem outro elemento que nao eh none
        if Parser.tokens.current != None and Parser.tokens.current.type != "CLOSE_PAR":
            raise ValueError(Parser.ERROR)
            
        return result

    def parse_rel_exp():
        pass

    def parse_statement():
        pass

    def parse_assignment():
        pass

    def parse_statments():
        pass

    def parse_print():
        pass

    def parse_if_else():
        pass

    def parse_while():
        pass


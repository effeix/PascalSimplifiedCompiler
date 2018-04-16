from tokenizer import Tokenizer
from binaryop import BinaryOp
from unaryop import UnaryOp
from program import Program

class Parser():
    ERROR = "Invalid token"

    term_ops = ["MULT", "DIV"]
    expression_ops = ["MINUS", "PLUS"]

    tokens = Tokenizer()

    def set_origin(origin):
        Parser.tokens.origin = origin 

    def parse():
        Parser.tokens.next()
        return Parser.parse_statetments()

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

    def parse_vardec():
        return 0

    def parse_funcdec():
        return 0

    def parse_program():
        if Parser.tokens.current.type == "PROGRAM":
            Parser.tokens.next()
            if Parser.tokens.current.type == "IDENTIFIER":
                Parser.tokens.next()
                if Parser.tokens.current.type == "STMT_FINISH":
                    result = Program()
                    result.set_child(Parser.parse_vardec())
                    result.set_child(Parser.parse_funcdec())
                    result.set_child(Parser.parse_statements())
                    return result 
                else:
                    raise ValuError(Parser.ERROR)
            else:
                raise ValueError(Parser.ERROR)
        else:
            raise ValueError(Parser.ERROR)

    def parse_statements():
        if Parser.tokens.current.type == "BEGIN":
            Parser.tokens.next()
            result = Parser.parse_statement()

            while Parser.tokens.current.type == "STMT_FINISH":
                result = Parser.parse_statement()

            if Parser.tokens.current.type == "END":
                raise ValueError(Parser.ERROR)
        else:
            raise ValueError(Parser.ERROR)

    def parse_print():
        pass

    def parse_if_else():
        pass

    def parse_while():
        pass


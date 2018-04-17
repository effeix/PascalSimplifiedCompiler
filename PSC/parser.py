from tokenizer import Tokenizer
from binaryop import BinaryOp
from unaryop import UnaryOp
from assignerop import AssignerOp
from wordresop import WordResOp
from printop import PrintOp
from stmtsop import StmtsOp
from program import Program
from intval import IntVal

class Parser():
    ERROR = "Invalid token"

    term_ops = ["MULT", "DIV"]
    expression_ops = ["MINUS", "PLUS"]

    tokens = Tokenizer()

    def set_origin(origin):
        Parser.tokens.origin = origin 

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
        
        elif Parser.tokens.current.type == "WORD":
            result = WordResOp(Parser.tokens.current.value)

            Parser.tokens.next()
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
        #GAMBIARRA, REMOVER
        #se eu to acabando a conta n tem um close parents e tem outro elemento que nao eh none
        if Parser.tokens.current != None and Parser.tokens.current.type != "CLOSE_PAR" and Parser.tokens.current.type != "STMT_FINISH":
            raise ValueError(Parser.ERROR)
            
        return result

    def parse_rel_exp():
        pass 

    def parse_assignment():
        print("parse_assignemnt")
        word = Parser.tokens.current.value
        
        Parser.tokens.next()

        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "ASSIGN":
            result = AssignerOp(word)
            
            Parser.tokens.next()
            print(Parser.tokens.current.value)
            result.set_child(Parser.parse_expression())

            return result
        else:
            raise ValueError(Parser.ERROR)
    
    def parse_print():
        print("parse_print")
        Parser.tokens.next()
        
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            result = PrintOp()

            Parser.tokens.next()
            result.set_child(Parser.parse_expression())
            
            if Parser.tokens.current == None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)
            
            Parser.tokens.next()
            return result
        
        else:
            raise ValueError(Parser.ERROR)


    def parse_if_else():
        pass

    def parse_while():
        pass


    def parse_statement():
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "WORD":
            return Parser.parse_assignment()
        elif Parser.tokens.current.type == "Print":
            return Parser.parse_print()
        elif Parser.tokens.current.type == "BEGIN":
            return Parser.parse_statements()
        else: #verificar
            return IntVal(0)
    

    def parse_statements():
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "BEGIN":      
            result = StmtsOp()

            Parser.tokens.next()
            result.set_child(Parser.parse_statement())

            while Parser.tokens.current.type == "STMT_FINISH":
                Parser.tokens.next()
                result.set_child(Parser.parse_statement())


            if Parser.tokens.current.type != "END":
                raise ValueError(Parser.ERROR)
            
            return result

        else:
            raise ValueError(Parser.ERROR)
    
    def parse_vardec():
        return 0

    def parse_funcdec():
        return 0

    def parse_program():
        print("parse_program")
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        if Parser.tokens.current.type == "PROGRAM":
            Parser.tokens.next()
            if Parser.tokens.current.type == "WORD":
                Parser.tokens.next()
                if Parser.tokens.current.type == "STMT_FINISH":
                    result = Program()

                    '''Parser.tokens.next()
                    result.set_child(Parser.parse_vardec()) #0 n tem eval
                    
                    Parser.tokens.next()
                    result.set_child(Parser.parse_funcdec())'''
                    
                    Parser.tokens.next()
                    result.set_child(Parser.parse_statements())
                    Parser.tokens.next()
                    if Parser.tokens.current == None or Parser.tokens.current.type != "DOT":
                        raise ValueError(Parser.ERROR)


                    return result 
                else:
                    raise ValueError(Parser.ERROR)
            else:
                raise ValueError(Parser.ERROR)
        else:
            raise ValueError(Parser.ERROR)

    def parse():
        Parser.tokens.next()
        return Parser.parse_program()

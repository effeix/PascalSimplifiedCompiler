from tokenizer import Tokenizer
from binaryop import BinaryOp
from unaryop import UnaryOp
from assignernode import AssignerNode
from identifiernode import IdentifierNode
from printnode import PrintNode
from statementsnode import StatementsNode
from nullnode import NullNode
from condnode import CondNode
from loopnode import LoopNode
from program import Program

class Parser():
    ERROR = "Invalid token"

    term_ops = ["MULT", "DIV"]
    expression_ops = ["MINUS", "PLUS", "OR", "AND"]
    expression_rel_ops = ["EQUAL", "MORE_THAN", "LESS_THAN"]
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
            result = IdentifierNode(Parser.tokens.current.value)

            Parser.tokens.next()
            return result

        else:
            raise ValueError(Parser.ERROR)          

    def parse_term():
        result = Parser.parse_factor()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.term_ops:
            result_cp = result
            print(Parser.tokens.current.type)
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
        #if Parser.tokens.current != None and Parser.tokens.current.type != "CLOSE_PAR" and Parser.tokens.current.type != "STMT_FINISH":
        #    raise ValueError(Parser.ERROR)
            
        return result

    def parse_rel_exp():
        result = Parser.parse_expression()
        
        while Parser.tokens.current != None and Parser.tokens.current.type in Parser.expression_rel_ops:
            result_cp = result
            
            
            result = BinaryOp(Parser.tokens.current.type)
            
            Parser.tokens.next()
            
            result.set_child(result_cp)
            result.set_child(Parser.parse_expression())
        
        return result

    def parse_assignment():
        word = Parser.tokens.current.value
        
        Parser.tokens.next()

        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "ASSIGN":
            result = AssignerNode(word)
            
            Parser.tokens.next()
            result.set_child(Parser.parse_expression())

            return result
        else:
            raise ValueError(Parser.ERROR)
    
    def parse_print():
        Parser.tokens.next()
        
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            result = PrintNode()

            Parser.tokens.next()
            result.set_child(Parser.parse_expression())
            
            if Parser.tokens.current == None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)
            
            Parser.tokens.next()
            return result
        
        else:
            raise ValueError(Parser.ERROR)


    def parse_if_else():
        Parser.tokens.next()
        
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)
        
        elif Parser.tokens.current.type == "OPEN_PAR":

            result = CondNode()
            
            Parser.tokens.next()

            result.set_child(Parser.parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()
                
                if Parser.tokens.current.type == "THEN":

                    Parser.tokens.next()
                
                    if Parser.tokens.current.type == "BEGIN":

                        result.set_child(Parser.parse_statements())
                        
                        if Parser.tokens.current.type == "ELSE":

                            Parser.tokens.next()

                            if Parser.tokens.current.type == "BEGIN":

                                result.set_child(Parser.parse_statements())
                        
                        else:
                            result.set_child(NullNode())

                    else:
                        raise ValueError(Parser.ERROR)
                else:
                    raise ValueError(Parser.ERROR)
                
            else:
                raise ValueError(Parser.ERROR)

        else:
            raise ValueError(Parser.ERROR)
        
        return result
                    


        

        

    def parse_while():
        Parser.tokens.next()
        
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)
        
        elif Parser.tokens.current.type == "OPEN_PAR":

            result = LoopNode()
            
            Parser.tokens.next()

            result.set_child(Parser.parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()
                
                if Parser.tokens.current.type == "DO":

                    Parser.tokens.next()
                
                    if Parser.tokens.current.type == "BEGIN":

                        result.set_child(Parser.parse_statements())

                    else:
                        raise ValueError(Parser.ERROR)
                else:
                    raise ValueError(Parser.ERROR)
                
            else:
                raise ValueError(Parser.ERROR)
        
        return result


    def parse_statement():
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)
        
        elif Parser.tokens.current.type == "IF":
            return Parser.parse_if_else()
        elif Parser.tokens.current.type == "WHILE":
            return Parser.parse_while()
        elif Parser.tokens.current.type == "WORD":
            return Parser.parse_assignment()
        elif Parser.tokens.current.type == "PRINT":
            return Parser.parse_print()
        elif Parser.tokens.current.type == "BEGIN":
            return Parser.parse_statements()
        else: #verificar
            return NullNode()
    

    def parse_statements():
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "BEGIN":      
            result = StatementsNode()

            Parser.tokens.next()
            result.set_child(Parser.parse_statement())

            while Parser.tokens.current.type == "STMT_FINISH":
                Parser.tokens.next()
                result.set_child(Parser.parse_statement())
     
            if Parser.tokens.current.type != "END":
                raise ValueError(Parser.ERROR)
            
            Parser.tokens.next()
            return result

        else:
            raise ValueError(Parser.ERROR)
    
    def parse_vardec():
        return 0

    def parse_funcdec():
        return 0

    def parse_program():
        if Parser.tokens.current == None:
            raise ValueError(Parser.ERROR)

        if Parser.tokens.current.type == "PROGRAM":
            Parser.tokens.next()
            if Parser.tokens.current.type == "WORD":
                Parser.tokens.next()
                if Parser.tokens.current.type == "STMT_FINISH":
                    result = Program()

                    #Parser.tokens.next()
                    #result.set_child(Parser.parse_vardec()) #0 n tem eval
                    
                    #Parser.tokens.next()
                    #result.set_child(Parser.parse_funcdec())
                    
                    Parser.tokens.next()
                    result.set_child(Parser.parse_statements())

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
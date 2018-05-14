from assignernode import AssignerNode
from binaryop import BinaryOp
from condnode import CondNode
from identifiernode import IdentifierNode
from loopnode import LoopNode
from nullnode import NullNode
from printnode import PrintNode
from program import Program
from statementsnode import StatementsNode
from tokenizer import Tokenizer
from unaryop import UnaryOp
from vardecnode import VarDecNode


class Parser():
    ERROR = "Invalid token"

    term_ops = ["MULT", "DIV", "AND"]
    expression_ops = ["MINUS", "PLUS", "OR", "NOT"]
    expression_rel_ops = ["EQUAL", "MORE_THAN", "LESS_THAN"]

    tokens = Tokenizer()

    def set_origin(origin):
        Parser.tokens.origin = origin

    def parse_factor():
        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()
            expr = Parser.parse_expression()

            if Parser.tokens.current is None \
                    or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)

            Parser.tokens.next()
            return expr

        elif Parser.tokens.current.type == "INT":
            result = BinaryOp(Parser.tokens.current.value)

            Parser.tokens.next()

            return result

        elif Parser.tokens.current.type == "TRUE" \
                or Parser.tokens.current.type == "FALSE":
            result = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            return result

        elif Parser.tokens.current.type in Parser.expression_ops:
            result = UnaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            result.set_child(Parser.parse_factor())

            return result

        elif Parser.tokens.current.type == "IDENTIFIER":
            result = IdentifierNode(Parser.tokens.current.value)

            Parser.tokens.next()
            return result

        else:
            raise ValueError(Parser.ERROR)

    def parse_term():
        result = Parser.parse_factor()

        while Parser.tokens.current is not None and \
                Parser.tokens.current.type in Parser.term_ops:
            result_cp = result
            result = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            result.set_child(result_cp)
            result.set_child(Parser.parse_factor())

        return result

    def parse_expression():
        result = Parser.parse_term()

        while Parser.tokens.current is not None \
                and Parser.tokens.current.type in Parser.expression_ops:
            result_cp = result

            result = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            result.set_child(result_cp)
            result.set_child(Parser.parse_term())

        # GAMBIARRA, REMOVER
        # se eu to acabando a conta n tem um close parents e tem outro elemento que nao eh none
        # if Parser.tokens.current != None and Parser.tokens.current.type != "CLOSE_PAR" and Parser.tokens.current.type != "SEMICOLON":
        #    raise ValueError(Parser.ERROR)

        return result

    def parse_rel_exp():
        result = Parser.parse_expression()

        while Parser.tokens.current is not None \
                and Parser.tokens.current.type in Parser.expression_rel_ops:
            result_cp = result

            result = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            result.set_child(result_cp)
            result.set_child(Parser.parse_expression())

        return result

    def parse_assignment():
        word = Parser.tokens.current.value

        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "ASSIGN":

            result = AssignerNode(_value=word)

            Parser.tokens.next()

            result.set_child(Parser.parse_expression())

            return result
        else:
            raise ValueError(Parser.ERROR)

    def parse_print():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            result = PrintNode()

            Parser.tokens.next()
            result.set_child(Parser.parse_expression())

            if Parser.tokens.current is None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)

            Parser.tokens.next()
            return result

        else:
            raise ValueError(Parser.ERROR)

    def parse_if_else():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(f"Wrong construction of IF-ELSE block.")

        elif Parser.tokens.current.type == "OPEN_PAR":

            result = CondNode()

            Parser.tokens.next()

            result.set_child(Parser.parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()

                if Parser.tokens.current.type == "THEN":

                    Parser.tokens.next()
                    result.set_child(Parser.parse_statements())

                    if Parser.tokens.current.type == "ELSE":

                        Parser.tokens.next()
                        result.set_child(Parser.parse_statements())

                    else:
                        result.set_child(NullNode())
                else:
                    raise ValueError(f"Expecting THEN keyword. Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return result

    def parse_while():
        Parser.tokens.next()

        if Parser.tokens.current is None:
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
        if Parser.tokens.current.type == "IF":
            return Parser.parse_if_else()
        elif Parser.tokens.current.type == "WHILE":
            return Parser.parse_while()
        elif Parser.tokens.current.type == "IDENTIFIER":
            return Parser.parse_assignment()
        elif Parser.tokens.current.type == "PRINT":
            return Parser.parse_print()
        elif Parser.tokens.current.type == "BEGIN":
            return Parser.parse_statements()
        else:
            return NullNode()

    def parse_statements():
        if Parser.tokens.current is None or Parser.tokens.current.type != "BEGIN":
            raise ValueError(f"Expecting BEGIN keyword. Got: {Parser.tokens.current.type}")

        elif Parser.tokens.current.type == "BEGIN":
            result = StatementsNode()

            Parser.tokens.next()

            result.set_child(Parser.parse_statement())

            while Parser.tokens.current.type == "SEMICOLON":
                Parser.tokens.next()
                result.set_child(Parser.parse_statement())

            if Parser.tokens.current.type != "END":
                raise ValueError(f"Expecting final END keyword. Got: {Parser.tokens.current.type}")

            Parser.tokens.next()

        return result

    def parse_vardec():
        f_lines = True
        result = NullNode()

        if Parser.tokens.current is None:
            raise ValueError(f"unexpected end of file")

        if Parser.tokens.current.type == "VAR":
            result = VarDecNode()

            Parser.tokens.next()

            while f_lines:
                variables = []

                if Parser.tokens.current.type == "IDENTIFIER":
                    variables.append(Parser.tokens.current.value)
                    Parser.tokens.next()

                    while Parser.tokens.current.type == "COMMA":
                        Parser.tokens.next()

                        if Parser.tokens.current.type == "IDENTIFIER":
                            variables.append(Parser.tokens.current.value)
                            Parser.tokens.next()
                        else:
                            raise ValueError(f"Expecting variable name after comma (,). Got: {Parser.tokens.current.type}")

                    if Parser.tokens.current.type == "COLON":
                        Parser.tokens.next()

                        if Parser.tokens.current.type == "BOOL" or Parser.tokens.current.type == "INTEGER":

                            for var in variables:
                                varnode = AssignerNode(_vartype=Parser.tokens.current.type, _value=var)
                                result.set_child(varnode)

                            Parser.tokens.next()

                            if Parser.tokens.current.type == "SEMICOLON":

                                Parser.tokens.next()

                                if Parser.tokens.current.type != "IDENTIFIER":
                                    f_lines = False
                            else:
                                raise ValueError(f"Expecting semicolon (;). Got: {Parser.tokens.current.type}")
                        else:
                            raise ValueError(f"Expecting variable type. Got: {Parser.tokens.current.type}")
                    else:
                        raise ValueError(f"Variable list should be followed by trailing colon (:). Got: {Parser.tokens.current.type}")
                else:
                    raise ValueError(f"Expecting variable name. Got: {Parser.tokens.current.type}")
        return result

    def parse_funcdec():
        pass

    def parse_program():
        if Parser.tokens.current is None:
            raise ValueError("File cannot be empty")

        if Parser.tokens.current.type == "PROGRAM":
            Parser.tokens.next()
            if Parser.tokens.current.type == "IDENTIFIER":
                Parser.tokens.next()
                if Parser.tokens.current.type == "SEMICOLON":
                    Parser.tokens.next()

                    result = Program()

                    result.set_child(Parser.parse_vardec())

                    result.set_child(Parser.parse_statements())

                    if Parser.tokens.current is None or \
                            Parser.tokens.current.type != "DOT":
                        raise ValueError(f"Expecting final dot (.). Got: {Parser.tokens.current.type}")
                else:
                    raise ValueError(f"Expecting semicolon (;). Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting program name. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting PROGRAM keyword. Got: {Parser.tokens.current.type}")

        return result

    def parse():
        Parser.tokens.next()
        return Parser.parse_program()

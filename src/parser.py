from assignernode import AssignerNode
from binaryop import BinaryOp
from blocknode import Block
from boolval import BoolVal
from condnode import CondNode
from funcdecnode import FuncDecNode
from identifiernode import IdentifierNode
from intval import IntVal
from loopnode import LoopNode
from nullnode import NullNode
from program import Program
from readnode import ReadNode
from statementsnode import StatementsNode
from tokenizer import Tokenizer
from unaryop import UnaryOp
from vardecnode import VarDecNode
from writenode import WriteNode


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
            node = IntVal(Parser.tokens.current.value)

            Parser.tokens.next()

            return node

        elif Parser.tokens.current.type == "BOOL":
            node = BoolVal(Parser.tokens.current.value)

            Parser.tokens.next()

            return node

        elif Parser.tokens.current.type in Parser.expression_ops:
            node = UnaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(Parser.parse_factor())

            return node

        elif Parser.tokens.current.type == "IDENTIFIER":
            node = IdentifierNode(Parser.tokens.current.value)

            Parser.tokens.next()
            return node

        else:
            raise ValueError(Parser.ERROR)

    def parse_term():
        node = Parser.parse_factor()

        while Parser.tokens.current is not None and \
                Parser.tokens.current.type in Parser.term_ops:
            node_cp = node
            node = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(node_cp)
            node.set_child(Parser.parse_factor())

        return node

    def parse_expression():
        node = Parser.parse_term()

        while Parser.tokens.current is not None \
                and Parser.tokens.current.type in Parser.expression_ops:
            node_cp = node

            node = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(node_cp)
            node.set_child(Parser.parse_term())

        return node

    def parse_rel_exp():
        node = Parser.parse_expression()

        while Parser.tokens.current is not None \
                and Parser.tokens.current.type in Parser.expression_rel_ops:
            node_cp = node

            node = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(node_cp)
            node.set_child(Parser.parse_expression())

        return node

    def parse_assignment():
        word = Parser.tokens.current.value

        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "ASSIGN":

            node = AssignerNode(_value=word)

            Parser.tokens.next()

            if Parser.tokens.current.type == "READ":
                node.set_child(Parser.parse_read())
            else:
                node.set_child(Parser.parse_expression())

        else:
            print(Parser.tokens.current.type)
            raise ValueError(Parser.ERROR)

        return node

    def parse_read():
        Parser.tokens.next()

        if Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()

            if Parser.tokens.current.type == "CLOSE_PAR":
                node = ReadNode()
                Parser.tokens.next()

            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return node

    def parse_write():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            node = WriteNode()

            Parser.tokens.next()
            node.set_child(Parser.parse_expression())

            if Parser.tokens.current is None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)

            Parser.tokens.next()
            return node

        else:
            raise ValueError(Parser.ERROR)

    def parse_if_else():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(f"Wrong construction of IF-ELSE block.")

        elif Parser.tokens.current.type == "OPEN_PAR":

            node = CondNode()

            Parser.tokens.next()

            node.set_child(Parser.parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()

                if Parser.tokens.current.type == "THEN":

                    Parser.tokens.next()
                    node.set_child(Parser.parse_statements())

                    if Parser.tokens.current.type == "ELSE":

                        Parser.tokens.next()
                        node.set_child(Parser.parse_statements())

                    else:
                        node.set_child(NullNode())
                else:
                    raise ValueError(f"Expecting THEN keyword. Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return node

    def parse_while():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":

            node = LoopNode()

            Parser.tokens.next()

            node.set_child(Parser.parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()

                if Parser.tokens.current.type == "DO":

                    Parser.tokens.next()

                    if Parser.tokens.current.type == "BEGIN":

                        node.set_child(Parser.parse_statements())
                    else:
                        raise ValueError(Parser.ERROR)
                else:
                    raise ValueError(Parser.ERROR)
            else:
                raise ValueError(Parser.ERROR)

        return node

    def parse_statement():
        if Parser.tokens.current.type == "IF":
            return Parser.parse_if_else()
        elif Parser.tokens.current.type == "WHILE":
            return Parser.parse_while()
        elif Parser.tokens.current.type == "IDENTIFIER":
            return Parser.parse_assignment()
        elif Parser.tokens.current.type == "WRITE":
            return Parser.parse_write()
        elif Parser.tokens.current.type == "BEGIN":
            return Parser.parse_statements()
        else:
            return NullNode()

    def parse_statements():
        if Parser.tokens.current is None or Parser.tokens.current.type != "BEGIN":
            raise ValueError(f"Expecting BEGIN keyword. Got: {Parser.tokens.current.type}")

        elif Parser.tokens.current.type == "BEGIN":
            node = StatementsNode()

            Parser.tokens.next()

            node.set_child(Parser.parse_statement())

            while Parser.tokens.current.type == "SEMICOLON":
                Parser.tokens.next()
                node.set_child(Parser.parse_statement())

            if Parser.tokens.current.type != "END":
                raise ValueError(f"Expecting final END keyword. Got: {Parser.tokens.current.type}")

            Parser.tokens.next()

        return node

    def parse_funcdec():
        f_has_function = True
        node = NullNode()

        while f_has_function:
            if Parser.tokens.current.type == "FUNCTION":
                Parser.tokens.next()

                if Parser.tokens.current.type == "IDENTIFIER":
                    Parser.tokens.next()

                    node = FuncDecNode()

                    if Parser.tokens.current.type == "OPEN_PAR":
                        Parser.tokens.next()

                        # node.set_child(Parser.parse_function_arguments())

                        if Parser.tokens.current.type == "CLOSE_PAR":
                            Parser.tokens.next()

                            if Parser.tokens.current.type == "COLON":
                                Parser.tokens.next()

                                if Parser.tokens.current.type == "INTEGER" \
                                        or Parser.tokens.current.type == "BOOLEAN":
                                    Parser.tokens.next()

                                    if Parser.tokens.current.type == "SEMICOLON":
                                        Parser.tokens.next()

                                        node.set_child(Parser.parse_block())
                                        Parser.tokens.next()

                                    else:
                                        raise ValueError("Expecting ;")

            elif Parser.tokens.current.type == "BEGIN":
                f_has_function = False

            else:
                raise ValueError(f"Invalid token {Parser.tokens.current.type}")

        return node

    def parse_vardec():
        f_lines = True

        if Parser.tokens.current is None:
            raise ValueError(f"unexpected end of file")

        node = VarDecNode()

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

                    if Parser.tokens.current.type == "BOOLEAN" or Parser.tokens.current.type == "INTEGER":

                        for var in variables:
                            varnode = AssignerNode(_vartype=Parser.tokens.current.type, _value=var)
                            node.set_child(varnode)

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
        return node

    def parse_block():
        node = Block()

        if Parser.tokens.current.type == "VAR":
            node.set_child(Parser.parse_vardec())
        else:
            node.set_child(NullNode())

        Parser.parse_funcdec()
        node.set_child(Parser.parse_statements())

        return node

    def parse_program():
        if Parser.tokens.current is None:
            raise ValueError("File cannot be empty")

        if Parser.tokens.current.type == "PROGRAM":
            Parser.tokens.next()
            if Parser.tokens.current.type == "IDENTIFIER":
                Parser.tokens.next()
                if Parser.tokens.current.type == "SEMICOLON":
                    Parser.tokens.next()

                    node = Program()

                    node.set_child(Parser.parse_block())

                    if Parser.tokens.current is None or \
                            Parser.tokens.current.type != "DOT":
                        raise ValueError(f"Expecting final dot (.). Got: {Parser.tokens.current.type}")
                else:
                    raise ValueError(
                        f"Fatal: Syntax error, \";\" expected"
                        + f" but \"{Parser.tokens.current.type}\" found")
            else:
                raise ValueError(
                    f"Fatal: Syntax error, \"IDENTIFIER\" expected"
                    + f" but \"{Parser.tokens.current.type}\" found")
        else:
            raise ValueError(
                f"Fatal: Syntax error, \"PROGRAM\" expected"
                + f" but \"{Parser.tokens.current.type}"
                + f" {Parser.tokens.current.value}\" found")

        return node

    def parse():
        Parser.tokens.next()
        return Parser.parse_program()

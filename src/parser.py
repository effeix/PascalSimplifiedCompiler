from assignernode import AssignerNode
from binaryop import BinaryOp
from blocknode import Block
from boolval import BoolVal
from condnode import CondNode
from funccallnode import FuncCallNode
from funcdecnode import FuncDecNode
from functionsnode import FunctionsNode
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

    def __parse_factor():
        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            Parser.tokens.next()
            expr = Parser.__parse_expression()

            if Parser.tokens.current is None \
                    or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)

            Parser.tokens.next()
            return expr

        elif Parser.tokens.current.type == "INT":
            node = IntVal(Parser.tokens.current.value)

            Parser.tokens.next()

        elif Parser.tokens.current.type == "BOOL":
            node = BoolVal(Parser.tokens.current.value)

            Parser.tokens.next()

        elif Parser.tokens.current.type in Parser.expression_ops:
            node = UnaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(Parser.__parse_factor())

        elif Parser.tokens.current.type == "IDENTIFIER":
            identifier = Parser.tokens.current.value
            node = IdentifierNode(Parser.tokens.current.value)

            Parser.tokens.next()

            if Parser.tokens.current.type == "OPEN_PAR":
                Parser.tokens.next()

                args = Parser.__parse_function_call_args()

                if Parser.tokens.current.type == "CLOSE_PAR":
                    node = FuncCallNode(identifier)
                    node.set_child(args)
                    Parser.tokens.next()

        else:
            raise ValueError(Parser.ERROR)

        return node

    def __parse_term():
        node = Parser.__parse_factor()

        while Parser.tokens.current is not None and \
                Parser.tokens.current.type in Parser.term_ops:
            node_cp = node
            node = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(node_cp)
            node.set_child(Parser.__parse_factor())

        return node

    def __parse_expression():
        node = Parser.__parse_term()

        while Parser.tokens.current is not None \
                and Parser.tokens.current.type in Parser.expression_ops:
            node_cp = node

            node = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(node_cp)
            node.set_child(Parser.__parse_term())

        return node

    def __parse_rel_exp():
        node = Parser.__parse_expression()

        while Parser.tokens.current is not None \
                and Parser.tokens.current.type in Parser.expression_rel_ops:
            node_cp = node

            node = BinaryOp(Parser.tokens.current.type)

            Parser.tokens.next()

            node.set_child(node_cp)
            node.set_child(Parser.__parse_expression())

        return node

    def __parse_assignment():
        word = Parser.tokens.current.value

        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "ASSIGN":

            node = AssignerNode(_value=word)

            Parser.tokens.next()

            if Parser.tokens.current.type == "READ":
                node.set_child(Parser.__parse_read())
            else:
                node.set_child(Parser.__parse_expression())

        else:
            raise ValueError(Parser.ERROR)

        return node

    def __parse_read():
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

    def __parse_write():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":
            node = WriteNode()

            Parser.tokens.next()
            node.set_child(Parser.__parse_expression())

            if Parser.tokens.current is None or Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError(Parser.ERROR)

            Parser.tokens.next()
            return node

        else:
            raise ValueError(Parser.ERROR)

    def __parse_if_else():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(f"Wrong construction of IF-ELSE block.")

        elif Parser.tokens.current.type == "OPEN_PAR":

            node = CondNode()

            Parser.tokens.next()

            node.set_child(Parser.__parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()

                if Parser.tokens.current.type == "THEN":

                    Parser.tokens.next()
                    node.set_child(Parser.__parse_statements())

                    if Parser.tokens.current.type == "ELSE":

                        Parser.tokens.next()
                        node.set_child(Parser.__parse_statements())

                    else:
                        node.set_child(NullNode())
                else:
                    raise ValueError(f"Expecting THEN keyword. Got: {Parser.tokens.current.type}")
            else:
                raise ValueError(f"Expecting closing parenthesis. Got: {Parser.tokens.current.type}")
        else:
            raise ValueError(f"Expecting opening parenthesis. Got: {Parser.tokens.current.type}")

        return node

    def __parse_while():
        Parser.tokens.next()

        if Parser.tokens.current is None:
            raise ValueError(Parser.ERROR)

        elif Parser.tokens.current.type == "OPEN_PAR":

            node = LoopNode()

            Parser.tokens.next()

            node.set_child(Parser.__parse_rel_exp())

            if Parser.tokens.current.type == "CLOSE_PAR":

                Parser.tokens.next()

                if Parser.tokens.current.type == "DO":

                    Parser.tokens.next()

                    if Parser.tokens.current.type == "BEGIN":

                        node.set_child(Parser.__parse_statements())
                    else:
                        raise ValueError(Parser.ERROR)
                else:
                    raise ValueError(Parser.ERROR)
            else:
                raise ValueError(Parser.ERROR)

        return node

    def __parse_statement():
        if Parser.tokens.current.type == "IF":
            return Parser.__parse_if_else()
        elif Parser.tokens.current.type == "WHILE":
            return Parser.__parse_while()
        elif Parser.tokens.current.type == "IDENTIFIER":
            return Parser.__parse_assignment()
        elif Parser.tokens.current.type == "WRITE":
            return Parser.__parse_write()
        elif Parser.tokens.current.type == "BEGIN":
            return Parser.__parse_statements()
        else:
            return NullNode()

    def __parse_statements():
        if Parser.tokens.current is None or Parser.tokens.current.type != "BEGIN":
            raise ValueError(f"Expecting BEGIN keyword. Got: {Parser.tokens.current.type}")

        elif Parser.tokens.current.type == "BEGIN":
            node = StatementsNode()

            Parser.tokens.next()

            node.set_child(Parser.__parse_statement())

            while Parser.tokens.current.type == "SEMICOLON":
                Parser.tokens.next()
                node.set_child(Parser.__parse_statement())

            if Parser.tokens.current.type != "END":
                raise ValueError(f"Expecting final END keyword. Got: {Parser.tokens.current.type} at {Parser.tokens.position}")

            Parser.tokens.next()

        return node

    def __parse_function_call_args():
        arguments = []
        while Parser.tokens.current.type != "CLOSE_PAR":
            argument = Parser.__parse_rel_exp()
            if isinstance(argument, BoolVal):
                arg_type = "BOOLEAN"
            elif isinstance(argument, IntVal):
                arg_type = "INTEGER"
            elif isinstance(argument, IdentifierNode):
                arg_type = "IDENTIFIER"

            arguments.append((argument, arg_type))

            if Parser.tokens.current.type == "COMMA":
                Parser.tokens.next()
            elif Parser.tokens.current.type != "CLOSE_PAR":
                raise ValueError("Invalid token")

        return arguments

    def __parse_funcdec():
        f_has_function = True
        node = FunctionsNode()

        while f_has_function:
            if Parser.tokens.current.type == "FUNCTION":
                Parser.tokens.next()

                if Parser.tokens.current.type == "IDENTIFIER":
                    func_name = Parser.tokens.current.value
                    Parser.tokens.next()

                    child_node = FuncDecNode(func_name)

                    if Parser.tokens.current.type == "OPEN_PAR":

                        arguments = Parser.__parse_vardec(is_parsing_function=True)

                        if Parser.tokens.current.type == "CLOSE_PAR":
                            Parser.tokens.next()

                            if Parser.tokens.current.type == "COLON":
                                Parser.tokens.next()

                                if Parser.tokens.current.type == "INTEGER" \
                                        or Parser.tokens.current.type == "BOOLEAN":

                                    return_type = Parser.tokens.current.type
                                    Parser.tokens.next()

                                    if Parser.tokens.current.type == "SEMICOLON":

                                        ret = AssignerNode(
                                            _vartype=return_type,
                                            _value=func_name
                                        )

                                        arguments.set_child(ret)

                                        Parser.tokens.next()

                                        child_node.set_child(arguments)
                                        child_node.set_child(Parser.__parse_block())
                                        node.set_child(child_node)

                                        Parser.tokens.next()

                                    else:
                                        raise ValueError("Expecting ;")

            elif Parser.tokens.current.type == "BEGIN":
                f_has_function = False

            else:
                raise ValueError(f"Invalid token {Parser.tokens.current.type}")

        return node

    def __parse_vardec(is_parsing_function=False):
        f_lines = True

        if Parser.tokens.current is None:
            raise ValueError(f"unexpected end of file")

        node = VarDecNode()

        last_token = Parser.tokens.current.type

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
                            if not is_parsing_function:
                                raise ValueError(f"Expecting semicolon (;). Got: {Parser.tokens.current.type}")
                            else:
                                break
                    else:
                        raise ValueError(f"Expecting variable type. Got: {Parser.tokens.current.type}")
                else:
                    raise ValueError(f"Variable list should be followed by trailing colon (:). Got: {Parser.tokens.current.type}")
            else:
                if last_token != "OPEN_PAR":
                    raise ValueError(f"Expecting variable name. Got: {Parser.tokens.current.type}")
                else:
                    break
        return node

    def __parse_block():
        node = Block()

        if Parser.tokens.current.type == "VAR":
            node.set_child(Parser.__parse_vardec())
        else:
            node.set_child(NullNode())

        node.set_child(Parser.__parse_funcdec())
        node.set_child(Parser.__parse_statements())

        return node

    def __parse_program():
        if Parser.tokens.current is None:
            raise ValueError("File cannot be empty")

        if Parser.tokens.current.type == "PROGRAM":
            Parser.tokens.next()
            if Parser.tokens.current.type == "IDENTIFIER":
                Parser.tokens.next()
                if Parser.tokens.current.type == "SEMICOLON":
                    Parser.tokens.next()

                    node = Program()

                    node.set_child(Parser.__parse_block())

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

    def parse(program=""):
        Parser.tokens.origin = program
        Parser.tokens.next()
        return Parser.__parse_program()

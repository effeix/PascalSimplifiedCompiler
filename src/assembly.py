CONSTANTS = [
    "SYS_EXIT equ 1",
    "SYS_READ equ 3",
    "SYS_WRITE equ 4",
    "STDIN equ 0",
    "STDOUT equ 1",
    "True equ 1",
    "False equ 0"
]

DATA_SEGMENT = "segment .data"

BSS_SEGMENT = "segment .bss"

PRINT_PROC = [
    "section .text",
    """  global _start""",
    "print:",
    """  POP EBX""",
    """  POP EAX""",
    """  PUSH EBX""",
    """  XOR ESI, ESI""",
    "print_dec:",
    """  MOV EDX, 0""",
    """  MOV EBX, 0x000A""",
    """  DIV EBX""",
    """  ADD EDX, '0'""",
    """  PUSH EDX""",
    """  INC ESI""",
    """  CMP EAX, 0""",
    """  JZ print_next""",
    """  JMP print_dec""",
    "print_next:",
    """  CMP ESI, 0""",
    """  JZ print_exit""",
    """  DEC ESI""",
    """  MOV EAX, SYS_WRITE""",
    """  MOV EBX, STDOUT""",
    """  POP ECX""",
    """  MOV [res], ECX""",
    """  MOV ECX, res""",
    """  MOV EDX, 1""",
    """  INT 0x80""",
    """  JMP print_next""",
    "print_exit:",
    """  RET"""
]

IF_WHILE_PROC = [
    "binop_je:",
    """  JE binop_true""",
    """  JMP binop_false""",
    "binop_jg:",
    """  JG binop_true""",
    """  JMP binop_false""",
    "binop_jl:",
    """  JL binop_true""",
    """  JMP binop_false""",
    "binop_false:",
    """  MOV EBX, False""",
    """  JMP binop_exit""",
    "binop_true:",
    """  MOV EBX, True""",
    "binop_exit:",
    """  RET"""
]

START = "_start:"

INTERRUPT = [
    """  MOV EAX, 1""",
    """  INT 0x80"""
]


class Assembly():
    __code = ""

    def __new__(cls):

        if not hasattr(cls, "__instance"):
            cls.__instance = super(Assembly, cls).__new__(cls)

        return cls.__instance

    @staticmethod
    def append(line):
        if isinstance(line, str):
            Assembly.__code += (line + "\n")
        elif isinstance(line, list):
            for l in line:
                Assembly.__code += (l + "\n")

    @staticmethod
    def code():
        print(Assembly.__code)

    @staticmethod
    def make_file():
        with open("psc.asm", "w") as f:
            f.write(Assembly.__code)
import sys
import os
from subprocess import call
from parser import Parser
from assembly import Assembly

ARGS = sys.argv


def read_pascal(f):
    with open(f, 'r') as ff:
        return ff.read().rstrip("\n")


def get_paths(filename):
    src_file = filename
    asm_file = src_file.replace(".pas", ".asm")
    obj_file = asm_file.replace(".asm", ".o")
    exe_file = obj_file.replace(".o", "")

    current_path = os.path.dirname(os.path.abspath(__file__))
    exe_path = os.path.dirname(current_path) + "/bin/"

    if not os.path.exists(exe_path):
        os.makedirs(exe_path)

    PATHS = {
        "src": src_file,
        "asm": exe_path + asm_file,
        "obj": exe_path + obj_file,
        "exe": exe_path + exe_file
    }

    return PATHS


def main():
    try:
        src_file = ARGS[1]
    except IndexError as e:
        sys.exit("Expecting pascal source file in position 1")

    try:
        exec_type = ARGS[2]
    except IndexError:
        exec_type = "i"

    Assembly.set_exec_type(exec_type)

    if exec_type in "ic":
        program = read_pascal(src_file).lower()
        Parser.parse(program).eval()
    else:
        sys.exit(f"Failed: expecting [i | c] in position 2 (got {exec_type})")

    if exec_type == "c":
        PATHS = get_paths(src_file)
        Assembly.print()
        Assembly.make_file(PATHS["asm"])

        try:
            call(["nasm", "-f", "elf32", "-o", PATHS["obj"], PATHS["asm"]])
        except:
            sys.exit(f"Can't create object file from {PATHS['asm']}")

        try:
            call(["ld", "-m", "elf_i386", "-s", "-o", PATHS["exe"], PATHS["obj"]])
        except:
            sys.exit(f"Can't create executable file from {PATHS['obj']}")

        call(["rm", f"{PATHS['asm']}", f"{PATHS['obj']}"])


if __name__ == "__main__":
    main()

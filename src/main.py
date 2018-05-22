import sys
from subprocess import call
from parser import Parser
from assembly import Assembly

ARGS = sys.argv
COMP = "../bin/"


def read_pascal(f):
    with open(f, 'r') as ff:
        return ff.read().rstrip("\n")


def main():
    src_filename = ARGS[1]
    asm_filename = COMP + src_filename.replace(".pas", ".asm")
    obj_filename = COMP + asm_filename.replace(".asm", ".o")
    exe_filename = COMP + obj_filename.replace(".o", "")

    try:
        exec_type = ARGS[2]
    except IndexError:
        exec_type = "i"

    origin = read_pascal(src_filename).lower()

    Parser.set_origin(origin)
    Parser.parse().eval()

    if exec_type == "c":
        Assembly.print()
        Assembly.make_file(asm_filename)

        try:
            call(["nasm", "-f", "elf32", "-o", obj_filename, asm_filename])
        except:
            sys.exit(f"Can't create object file from {asm_filename}")

        try:
            call(["ld", "-m", "elf_i386", "-s", "-o", exe_filename, obj_filename])
        except:
            sys.exit(f"Can't create executable file from {obj_filename}")

        call(["rm", f"{asm_filename}", f"{obj_filename}"])


if __name__ == "__main__":
    main()

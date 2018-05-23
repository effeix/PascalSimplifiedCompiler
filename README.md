# Pascal Simplified Compiler

### Usage
You are free to use PSC however you like. Simply clone the repository and run the file ```main.py``` (inside ```src/``` dir):

```sh
$ python3 src/main.py PASCAL_FILE i|c
```

where ```i``` stands for the interpreted version and ```c``` for the compiled version.

##### Dependencies
- Python 3.6.x
- NASM command line tool
- GNU Linker

### Features
###### Features marked with "!" are currently being implemented
- [x] Lexical Analysis
- [x] Syntactic Analysis
- [x] Addition / Subtraction
- [x] Multiplication / Division
- [x] Comments
- [x] Syntatic Errors
- [x] Parenthesis
- [x] Unary Operators
- [x] Abstract Syntax Tree
- [x] Program Flow
- [x] Keywords
- [x] Variables
- [x] Symbol Table
- [x] Print
- [x] Boolean Operators
- [x] Conditional Statements
- [x] Loops
- [x] Read
- [x] Variable Declaration
- [x] Types
- [x] Type checking
- [x] Semantic Errors
- [x] Functions
- [x] Function Arguments
- [x] Variable Scopes
- [ ] Code Generation !

### EBNF
An [EBNF (<b>E</b>xtended <b>B</b>ackus-<b>N</b>aur <b>F</b>orm)](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form) is a sequence of statements describing a [Context-Free Grammar](https://en.wikipedia.org/wiki/Context-free_grammar). It is used to represent a formal language or programming language and, as the name sugests, is an extension to the original [BNF (<b>B</b>ackus-<b>N</b>aur <b>F</b>orm)](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form).

Below is the EBNF for this compiler:
```ebnf
program = "program", identifier, ";", block, ".";
block = ["var", varblock], [funcblock], statements;
var_declaration = identifier, {",", identifier}, ":", type;
varblock = var_declaration, {";", var_declaration};
funcblock = "function", identifier, "(", {var_declaration}, ")", ":", type, ";", block;
statements = "begin", statement, {";", statement}, [";"], "end";
statement = attribution | statements | print | if | while;
if = "if", expression, "then", statement, ["else", statement];
while = "while", expression, "do", statement;
attribution = identifier, ":=", expression | read;
read = "read", "(", ")";
print = "print", "(", expression, ")";
expression = simple_expression, {("<" | ">" | "="), simple_expression};
simple_expression = term, {("+" | "-" | "or"), term};
term = factor, {("*", "/", "and"), factor};
factor = ({"+" | "-" | "not"}, factor) | number | ("(", expression, ")") | identifier | funccall;
funccall = identifier, "(", [expression, {";", expression}], ")";
identifier = letter, {letter | digit | "_" };
number = digit, {digit};
letter = a .. z | A .. Z;
digit = 0 .. 9;
type = "bool" | "integer";
```

### Syntactic Diagram
The syntactic diagram is a visual representation of the EBNF, describing the algorithm used by the compiler. If you pay close attention to the code, you will se the similarities between the diagram and the algorithm. Below is the syntactic diagram for this compiler:

![Syntactic Diagram](https://i.imgur.com/zgaumZ6.png)

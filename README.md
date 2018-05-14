# Pascal Simplified Compiler

### Features (in order of implementation)
- [x] Lexical Analysis
- [x] Syntatic Analysis
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
- [ ] Read
- [x] Variable Declaration
- [-] Types
- [x] Semantic Errors
- [ ] Functions
- [ ] Function Arguments
- [ ] Variable Scopes
- [ ] Assembler

### EBNF
An EBNF (<b>E</b>xtended <b>B</b>ackus-<b>N</b>aur <b>F</b>orm) is a sequence of statements describing a [Context-Free Grammar](https://en.wikipedia.org/wiki/Context-free_grammar). It is used to represent a formal language or programming language and as the name sugests, is an extension to the original [BNF (<b>B</b>ackus-<b>N</b>aur <b>F</b>orm)](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form).
###### Reference: [Extended Backus-Naur Form on Wikipedia](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)

Below is the EBNF for this compiler:
```
program = "program", identifier, ";", block, ".";
block = [varblock], [funcblock], statements;
var_declaration = identifier, {",", identifier}, ":", type;
varblock = "var", var_declaration, {";", var_declaration};
funcblock = "function", identifier, "(", {var_declaration}, ")", ":", type, ";", block;
statements = "begin", statement, {";", statement}, [";"], "end";
statement = attribution | statements | print | if | while;
if = "if", expression, "then", statement, ["else", statement];
while = "while", expression, "do", statement;
attribution = identifier, ":=", expression | read;
read = "read", "(", ")";
print = "print", "(", expression, ")";
simple_expression = term, {("+" | "-" | "or"), term};
expression = simple_expression, {("<" | ">" | "="), simple_expression};
term = factor, {("*", "/", "and"), factor};
factor = ({"+" | "-" | "not"}, factor) | number | ("(", expression, ")") | identifier;
identifier = letter, {letter | digit | "_" };
number = digit, {digit};
letter = a .. z | A .. Z;
digit = 0 .. 9;
type = "bool" | "integer";
```

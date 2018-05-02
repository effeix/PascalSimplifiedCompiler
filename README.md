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
- [ ] Variable Declaration
- [ ] Types
- [ ] Semantic Errors
- [ ] Functions
- [ ] Function Arguments
- [ ] Variable Scopes
- [ ] Assembler

### EBNF
```
program = "program", identifier, ";", block, ".";
block = [varblock], [funcblock], statements;
var_declaration = identifier, {",", identifier}, ":", type;
varblock = "var", var_declaration, {";", var_declaration};
funcblock = "function", identifier, "(", {var_declaration}, ")", ":", type, ";", block;
statements = "begin", statement, {";", statement} [";"] "end";
statement = attribution | statements | print | if | while;
if = "if", expression, "then", statement, "else", statement;
while = "while", expression, 
attribution = identifier, ":=", expression | read;
read = "read", "(", ")";
print = "print", "(", simple_expression, ")";
simple_expression = term, { ("+", "-", "or"), term };
term = factor, { ("*", "/", "and"), factor };
factor = (("+", "-", "not"), factor) | number | ("(", expression, ")") | identifier;
identifier = letter, {letter | digit | "_" };
number = digit, { digit };
letter = (a .. z | A .. Z);
digit = (0 .. 9);
type = "bool" | "integer";
```

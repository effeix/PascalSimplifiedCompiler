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
- [ ] Program Flow
- [ ] Keywords
- [ ] Variables
- [ ] Symbol Table
- [ ] Print
- [ ] Boolean Operators
- [ ] Conditional Statements
- [ ] Loops
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
commands = "begin", command, {";", command} [";"] "end";
command = attribution | commands | print;
attribution = identifier, ":=", expression;
print = "print", "(", expression, ")";
expression = term, { ("+","-"), term };
term = factor, { ("*", "/"), factor };
factor = ("+", "-"), factor | number | "(", expression, ")" | identifier;
identifier = letter, {letter | digit | "_" };
number = digit, { digit };
letter = ( a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z );
digit = ( 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 )
```

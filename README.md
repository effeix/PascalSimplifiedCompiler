# Pascal Simplified Compiler

### Features (in order of implementation)
- [x] Lexical Analysis
- [x] Syntatic Analysis
- [x] Addition / Subtraction
- [x] Multiplication / Division
- [x] Comments
- [x] Syntatic Errors
- [] Parenthesis
- [] Reserved words
- [] Print
- [] Variables
- [] Functions and procedures
- [] Scope
- [] Conditional statements
- [] Loops
- [] Read
- [] Types
- [] Semantic Errors

### EBNF
```ebnf
expression = term(('+','-')term)*
term = num(('*','/')num)*
```
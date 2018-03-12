# Pascal Simplified Compiler

### Features (in order of implementation)
- [x] Lexical Analysis
- [x] Syntatic Analysis
- [x] Addition / Subtraction
- [x] Multiplication / Division
- [x] Comments
- [x] Syntatic Errors
- [ ] Parenthesis
- [ ] Unary Operators
- [ ] Abstract Syntax Tree
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
expression = term(('+','-')term)*
term = num(('*','/')num)*
```

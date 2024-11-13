# Programming Assignment 2 - Parser for Matrix Language
# Partners: Amanda Jenkins (alj2155) & Mike Yang (ty2467) 

## Context-Free Grammar Defined 

**Non-terminals:**
- PROGRAM: Represents the entire program.
- STATEMENT: Represents a single statement, which could be an assignment or display.
- MATRIX_ASSIGNMENT: Represents the assignment of a matrix literal to an identifier.
- MATRIX_MULT_ASSIGNMENT: Represents the assignment of the result of a matrix multiplication to an identifier.
- DISPLAY_STATEMENT: Represents the display of a matrix.
- MATRIX: Represents a matrix literal.
- IDENTIFIER: Represents an identifier (variable name).

**Terminals:**
- ID: Identifier, such as A, B, or C
- ASSIGN: Assignment operator =
- MATRIX: Matrix dimensions, ex. (1,2) or (3,4)
- OP_MUL: Multiplication operator x
- DISPLAY: Display keyword


**Production Rules:**

program -> statements 

statements -> statement statements | ε

statement -> matrix_assignment | maxtrix_mult_assignment | display_statement 

matrix_assignment -> id = matrix

Matrix -> matrix_row

Matrix_row -> (number, number) matrix_row| ε

maxtrix_mult_assignment -> id = id x id 

display_statement -> display id 

id -> A | B | C | D | E 

number -> int 






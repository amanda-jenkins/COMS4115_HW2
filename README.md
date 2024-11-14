# Programming Assignment 2 - Parser for Matrix Language
## Partners: Amanda Jenkins (alj2155) & Mike Yang (ty2467) 

## Context-Free Grammar Defined 

### Non-terminals: 
- program
  - The starting symbol of the CFG, representing the overall structure of our matrix program. 
    - program -> statements 
- statements
  -  Represents a sequence of statements in the program, allowing multiple statements to be chained.
    - statements -> statement statements | ε
- statement
  - Represents a single statement, which can be a matrix assignment, matrix multiplication assignment, OR display statement.
    - statement -> matrix_assignment | matrix_mult_assignment | display_statement
- matrix_assignment
  - The assignment of values to a matrix variable. 
    - matrix_assignment -> id = matrix
- matrix
  - The matrix structure consisting of multiple rows.
    - matrix -> matrix_row
- matrix_row
  - Each row in the matrix as a pair of numbers. 
    - matrix_row -> (number, number) matrix_row| ε
- matrix_mult_assignment
  - Assignment of a matrix multiplication result to a variable.
    - maxtrix_mult_assignment -> id = id x id 
- display_statement
  - Display of a matrix variable's values.
    - display_statement -> display id 
- id
  - Matrix variables, represented as letters.
    - id -> A | B | C | D | E
- number
  -  An integer number within the matrix rows.
    - number -> int

### Terminals:
- = (assignment operator)
- x (multiplication operator)
- display (keyword for display statements)
- A, B, C, D, E (identifiers for matrices)
- (  ) (parentheses for matrix entries, encloses the matrix values)
- , (comma used to separate values within a matrix row)
- int (integer values)


###  Production Rules:
- program -> statements 
- statements -> statement statements | ε
- statement -> matrix_assignment | maxtrix_mult_assignment | display_statement 
- matrix_assignment -> id = matrix
- matrix -> matrix_row
- matrix_row -> (number, number) matrix_row| ε
- maxtrix_mult_assignment -> id = id x id 
- display_statement -> display id 
- id -> A | B | C | D | E 
- number -> int 

### Sample Input Programs


### How to Run

1. Run the Scanner: Use the run_scanner.sh script to generate tokens for the sample code in example.txt. 
- chmod +x run_scanner.sh
- ./run_scanner.sh example.txt > tokens.txt
  - I will be redirecting the scanner’s output (tokens) to a file named tokens.txt
2. Run python3 parser_1.py


### Demo Video Link & Description






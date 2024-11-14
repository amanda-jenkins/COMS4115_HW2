# Programming Assignment 2 - Parser for Matrix Language
## Partner: Amanda Jenkins (alj2155) - updated group as suggested by TAs

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

1. 
Input Program (just assignment statements):  
A = (1,2)
    (3,4)
B = (5,6)
    (7,8)
C = A x B


Expected AST: 
'PROGRAM'
    'STATEMENTS'
        'MATRIX_ASSIGNMENT'
            'ID' (A)
            'MATRIX'
                'MATRIX_ROW' ('1', '2')
                'MATRIX_ROW' ('3', '4')
        'MATRIX_ASSIGNMENT'
            'ID' (B)
            'MATRIX'
                'MATRIX_ROW' ('5', '6')
                'MATRIX_ROW' ('7', '8')
        'MATRIX_MULT_ASSIGNMENT'
            'ID' (A)
            'ID' (B)
            'ID' (C)


2. 
Input Program (multiple matrix assignments, matrix multiplication assignment): 
A = (2,3)
    (4,5)
B = (1,1)
C = A x B
D = (3,3)
display D

Expected AST:
'PROGRAM'
    'STATEMENTS'
        'MATRIX_ASSIGNMENT'
            'ID' (A)
            'MATRIX'
                'MATRIX_ROW' ('2', '3')
                'MATRIX_ROW' ('4', '5')
        'MATRIX_ASSIGNMENT'
            'ID' (B)
            'MATRIX'
                'MATRIX_ROW' ('1', '1')
        'MATRIX_MULT_ASSIGNMENT'
            'ID' (A)
            'ID' (B)
            'ID' (C)
        'MATRIX_ASSIGNMENT'
            'ID' (D)
            'MATRIX'
                'MATRIX_ROW' ('3', '3')
        'DISPLAY_STATEMENT'
            'ID' (D)


3. 

Input Program (Error- Missing Assignment Operator): 
A (1,2)
    (3,4)
B = (5,6)
    (7,8)
C = A x B
display C

ERROR: SyntaxError: Expected '=' after 'A' in MATRIX_ASSIGNMENT

4. 

Input Program (missing matrix multiplication operator x): 
A = (1,2)
    (3,4)
B = (5,6)
    (7,8)
C = A B
display C

ERROR: SyntaxError: Expected 'x' operator for matrix multiplication between 'A' and 'B'


5. 
Input Program (display statements only): 
A = (1,0)
B = (2,2)
C = A x B
display A
display C

Expected AST:
'PROGRAM'
    'STATEMENTS'
        'MATRIX_ASSIGNMENT'
            'ID' (A)
            'MATRIX'
                'MATRIX_ROW' ('1', '0')
        'MATRIX_ASSIGNMENT'
            'ID' (B)
            'MATRIX'
                'MATRIX_ROW' ('2', '2')
        'MATRIX_MULT_ASSIGNMENT'
            'ID' (A)
            'ID' (B)
            'ID' (C)
        'DISPLAY_STATEMENT'
            'ID' (A)
        'DISPLAY_STATEMENT'
            'ID' (C)


### How to Run

1. Run the Scanner: Use the run_scanner.sh script to generate tokens for the sample code in example.txt. 
- chmod +x run_scanner.sh
- ./run_scanner.sh example.txt > tokens.txt 
  - Our program redirects the scanner’s output (tokens) to a file named tokens.txt
  - Edit example.txt with a sample input program 
2. Run python3 parser_1.py


### Demo Video Link 
https://drive.google.com/drive/folders/1PHJg_KoF7VO697X8WO1n-cj4m4KZrQ40?usp=sharing





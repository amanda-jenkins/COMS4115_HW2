def read_tokens_from_file(filename):
    tokens = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                tokens.append((parts[0], parts[1]))
            elif len(parts) == 1:
                tokens.append((parts[0], None))
    return tokens

# this reads the tokens from tokens.txt
tokens = read_tokens_from_file("tokens.txt")

class Node:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self, level=0):
        ret = "\t" * level + repr(self.type)
        if self.value:
            ret += f" ({self.value})"
        ret += "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = 0

    def parse(self):
        return self.program()

    def program(self):
        # program -> statements
        node = Node("PROGRAM")
        statements_node = self.statements()
        if statements_node:
            node.add_child(statements_node)
        return node

    def statements(self):
        # statements -> statement statements | ε
        node = Node("STATEMENTS")
        while self.current_token < len(self.tokens) and self.tokens[self.current_token][0] != "EOF":
            statement_node = self.statement()
            if statement_node:
                node.add_child(statement_node)
        return node

    def statement(self):
        # statement -> matrix_assignment | matrix_mult_assignment | display_statement
        token_type, token_value = self.tokens[self.current_token]
        
        if token_type == "ID" and self.look_ahead(1)[0] == "ASSIGN":
            return self.matrix_assignment()
        elif token_type == "DISPLAY":
            return self.display_statement()
        elif token_type == "ID" and self.look_ahead(1)[0] == "MULT":
            return self.matrix_mult_assignment()
        return None

    def matrix_assignment(self):
        # matrix_assignment -> id = matrix
        node = Node("MATRIX_ASSIGNMENT")
        id_node = Node("ID", self.tokens[self.current_token][1])
        node.add_child(id_node)
        self.current_token += 2  
        
        matrix_node = self.matrix()
        if matrix_node:
            node.add_child(matrix_node)
        return node

    def matrix(self):
        # Matrix -> matrix_row
        node = Node("MATRIX")
        row_node = self.matrix_row()
        if row_node:
            node.add_child(row_node)
        return node

    def matrix_row(self):
        # Matrix_row -> (number, number) matrix_row | ε
        node = Node("MATRIX_ROW")
        while self.current_token < len(self.tokens) and self.tokens[self.current_token][0] == "LPAREN":
            self.current_token += 1  # Skip LPAREN
            number1 = self.tokens[self.current_token][1]
            self.current_token += 1  # Skip first number
            self.current_token += 1  # Skip COMMA
            number2 = self.tokens[self.current_token][1]
            self.current_token += 1  # Skip second number
            row_node = Node("ROW", (number1, number2))
            node.add_child(row_node)
            self.current_token += 1  # Skip RPAREN
        return node

    def matrix_mult_assignment(self):
        # matrix_mult_assignment -> id = id x id
        node = Node("MATRIX_MULT_ASSIGNMENT")
        id1_node = Node("ID", self.tokens[self.current_token][1])
        node.add_child(id1_node)
        self.current_token += 2  # Skip ID and ASSIGN

        id2_node = Node("ID", self.tokens[self.current_token][1])
        node.add_child(id2_node)
        self.current_token += 2  # Skip first ID and MULT

        id3_node = Node("ID", self.tokens[self.current_token][1])
        node.add_child(id3_node)
        self.current_token += 1  # Skip second ID
        return node

    def display_statement(self):
        # display_statement -> display id
        node = Node("DISPLAY_STATEMENT")
        self.current_token += 1  # Skip DISPLAY
        id_node = Node("ID", self.tokens[self.current_token][1])
        node.add_child(id_node)
        self.current_token += 1  # Skip ID
        return node

    def look_ahead(self, n):
        if self.current_token + n < len(self.tokens):
            return self.tokens[self.current_token + n]
        return None

    def parse_tokens(self, tokens):
        self.tokens = tokens
        self.current_token = 0
        ast = self.parse()
        return ast


# Example usage with tokens (to be generated from scanner output), if needed 


tokens = [
    ("ID", "A"), ("ASSIGN", "="), ("LPAREN", "("), ("NUMBER", "1"), ("COMMA", ","), ("NUMBER", "2"), ("RPAREN", ")"),
    ("ID", "B"), ("ASSIGN", "="), ("LPAREN", "("), ("NUMBER", "3"), ("COMMA", ","), ("NUMBER", "4"), ("RPAREN", ")"),
    ("ID", "C"), ("ASSIGN", "="), ("ID", "A"), ("MULT", "x"), ("ID", "B"),
    ("DISPLAY", "display"), ("ID", "C"), ("EOF", None)
]

parser = Parser(tokens)
ast = parser.parse_tokens(tokens)
print(ast)

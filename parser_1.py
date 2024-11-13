class Token:
    def __init__(self, type, value):
        self.type = type 
        self.value = value

    def __repr__(self):
        return "{}({})".format(self.type, self.value)



class ProgramNode:
    def __init__(self, statements):
        self.statements = statements

    def __str__(self, level=0):
        result = "  " * level + "PROGRAM\n"
        for stmt in self.statements:
            result += stmt.__str__(level + 1)
        return result


class AssignmentNode:
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

    def __str__(self, level=0):
        result = "  " * level + "MATRIX_ASSIGNMENT\n"
        result += "  " * (level + 1) + "IDENTIFIER({})\n".format(self.identifier.value)
        result += self.value.__str__(level + 1)
        return result


class DisplayNode:
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self, level=0):
        result = "  " * level + "DISPLAY_STATEMENT\n"
        result += "  " * (level + 1) + "IDENTIFIER({})\n".format(self.identifier.value)
        return result


class MatrixNode:
    def __init__(self, rows):
        self.rows = rows

    def __str__(self, level=0):
        result = "  " * level + "MATRIX_LIST\n"
        for row in self.rows:
            result += "  " * (level + 1) + "MATRIX({})\n".format(row)
        return result


class ExpressionNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self, level=0):
        result = "  " * level + "MATRIX_MULT_ASSIGNMENT\n"
        result += "  " * (level + 1) + "IDENTIFIER({})\n".format(self.left.value)
        result += "  " * (level + 1) + "OP_MUL({})\n".format(self.operator)
        result += "  " * (level + 1) + "IDENTIFIER({})\n".format(self.right.value)
        return result


# here is our parser class 
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def peek(self, offset=0):
        # implements lookahead
        pos = self.current + offset
        return self.tokens[pos] if pos < len(self.tokens) else None

    def advance(self):
        self.current += 1

    def match(self, expected_type):
        if self.peek() and self.peek().type == expected_type:
            token = self.peek()
            self.advance()
            return token
        else:
            raise SyntaxError("Expected {}, found {}".format(expected_type, self.peek().type if self.peek() else 'EOF'))

    def parseProgram(self):
        statements = []
        while self.peek() is not None:
            statements.append(self.parseStatement())
        return ProgramNode(statements)

    def parseStatement(self):
        if self.peek().type == 'ID' and self.peek(1).type == 'ASSIGN':
            return self.parseAssignment()
        elif self.peek().type == 'DISPLAY':
            return self.parseDisplayStatement()
        else:
            raise SyntaxError("Unexpected token in statement")

    def parseAssignment(self):
        identifier = self.match('ID')
        self.match('ASSIGN')
        if self.peek().type == 'MATRIX':
            return AssignmentNode(identifier, self.parseMatrixList())
        elif self.peek().type == 'ID' and self.peek(1).type == 'OP_MUL':
            return AssignmentNode(identifier, self.parseExpression())
        else:
            raise SyntaxError("Expected matrix or expression after assignment")

    def parseMatrixList(self):
        rows = []
        while self.peek().type == 'MATRIX':
            rows.append(self.match('MATRIX').value)
        return MatrixNode(rows)

    def parseExpression(self):
        left = self.match('ID')
        self.match('OP_MUL')
        right = self.match('ID')
        return ExpressionNode(left, 'x', right)

    def parseDisplayStatement(self):
        self.match('DISPLAY')
        identifier = self.match('ID')
        return DisplayNode(identifier)


# Example usages 
tokens = [
    Token('ID', 'A'), Token('ASSIGN', '='), Token('MATRIX', '(1,2)'), Token('MATRIX', '(3,4)'),
    Token('ID', 'B'), Token('ASSIGN', '='), Token('MATRIX', '(5,6)'), Token('MATRIX', '(7,8)'),
    Token('ID', 'C'), Token('ASSIGN', '='), Token('ID', 'A'), Token('OP_MUL', 'x'), Token('ID', 'B'),
    Token('DISPLAY', 'display'), Token('ID', 'C')
]

parser = Parser(tokens)
try:
    ast = parser.parseProgram()
    print(ast)
except SyntaxError as e:
    print("Syntax error:", e)

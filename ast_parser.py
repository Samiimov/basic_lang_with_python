from token import Token
# TOKEN TYPES
T_PLUS = "+"
T_MINUS = "-"
T_DIVISION = "/"
T_MULTIPLY = "*"
T_SEPARATOR = "\n"
T_NUMBER = "NUMBER"
T_STRING = "STRING"
# PARENTHESIS
LPAREN = "("
RPAREN = ")"

class Parser:
    def __init__(self):
        self.tokens = []
        self.current_token = None
        self.index = 0

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.index += 1
            try:
                self.current_token = self.tokens[self.index]
            except IndexError:
                return Token(None, None) # Return None token to end
        else:
            self.error()

    def factor(self):
        """factor : T_NUMBER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == T_NUMBER:
            self.eat(T_NUMBER)
            return Num(token)
        elif token.type == T_STRING:
            pass
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node

    def term(self):
        """term : factor ((T_MULTIPLY | T_DIVISION) factor)*"""
        node = self.factor()

        while self.current_token.type in (T_MULTIPLY, T_DIVISION):
            token = self.current_token
            if token.type == T_MULTIPLY:
                self.eat(T_MULTIPLY)
            elif token.type == T_DIVISION:
                self.eat(T_DIVISION)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expresion(self):
        """
        expr   : term ((T_PLUS | T_MINUS) term)
        term   : factor ((T_MULTIPLY | T_DIVISION) factor)
        factor : T_NUMBER | LPAREN expr RPAREN
        """
        node = self.term()

        while self.current_token.type in (T_PLUS, T_MINUS):
            token = self.current_token
            if token.type == T_PLUS:
                self.eat(T_PLUS)
            elif token.type == T_MINUS:
                self.eat(T_MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens[0]
        self.tree = self.expresion()
        return self.tree

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self) -> str:
        return f"BinOp({self.left}, {self.op}, {self.left})"

class Num:
    def __init__(self, token):
        self.token = token.type
        self.value = token.value

    def __repr__(self) -> str:
        return f"Num(Value : {self.value}, Token : {self.token})"
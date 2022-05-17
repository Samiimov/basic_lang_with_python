from lexer_token import Token
from variables import Variables

class Parser(Variables):
    def __init__(self):
        self.tokens = []
        self.current_token = None
        self.index = 0

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        """
        Move to next token in tokens list
        """
        if self.current_token.type == token_type:
            self.index += 1
            try:
                self.current_token = self.tokens[self.index]
            except IndexError:
                self.current_token = Token("None", None) # Return None token to end
        else:
            self.error()

    def factor(self):
        """
        Produce factor for AST
        """
        token = self.current_token
        if token.type == self.T_NUMBER:
            self.eat(self.T_NUMBER)
            return Num(token)
        elif token.type == self.T_VARIABLE:
            self.eat(self.T_VARIABLE)
            return Variable(token)
        elif token.type == self.LPAREN:
            self.eat(self.LPAREN)
            node = self.expresion()
            self.eat(self.RPAREN)
            return node

    def term(self):
        """
        Produce term for AST
        """
        node = self.factor()

        while self.current_token.type in (self.T_MULTIPLY, self.T_DIVISION):
            token = self.current_token
            if token.type == self.T_MULTIPLY:
                self.eat(self.T_MULTIPLY)
            elif token.type == self.T_DIVISION:
                self.eat(self.T_DIVISION)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expresion(self):
        """
        Produce expression for AST
        """
        node = self.term()

        while self.current_token.type in (self.T_PLUS, self.T_MINUS):
            token = self.current_token
            if token.type == self.T_PLUS:
                self.eat(self.T_PLUS)
            elif token.type == self.T_MINUS:
                self.eat(self.T_MINUS)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self, tokens):
        self.tokens = tokens
        self.current_token = self.tokens[0]
        self.tree = self.expresion()
        self.index = 0
        return self.tree

    def show_tree(self):
        print(self.tree)

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self) -> str:
        return f"BinOp( {self.left}, {self.op}, {self.right} )"

class Num:
    def __init__(self, token):
        self.token = token.type
        self.value = token.value

    def __repr__(self) -> str:
        return f"Num( Value : {self.value}, Token : {self.token} )"

class Str:
    def __init__(self, token):
        self.token = token.type
        self.value = token.value

    def __repr__(self) -> str:
        return f"Str( Value : {self.value}, Token : {self.token} )"

class Variable:
    def __init__(self, token) -> None:
        self.value = token.value
        self.token = token.type
        self.name = token.name

    def __repr__(self) -> None:
        return f"Var( Value : {self.value}, Token : {self.token}, Name : {self.name})"
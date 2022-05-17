from typing import List, Tuple
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

class Lexer:
    def __init__(self) -> None:
        self.tokens = []
        self.current_literal = ""
        self.pos = 0
        self.input = ""

    def next_char(self):
        """
        Move to next character in input str
        """
        self.pos += 1
        if self.pos == len(self.input):
            self.current_char = None
        else:
            self.current_char = self.input[self.pos]

    def tokenize(self, input : str) -> List[Token]:
        """
        Convert input string into list of tuples. 
        Tuple contasn token type and values.
        Params: 
            input, str : User's input
        Return:
            tokens, list[tuple] : List of tokens.
        """
        self.input = input
        self.current_char = input[self.pos]
        while self.current_char != None:
            if self.current_char == T_PLUS:
                self.add_tokens(T_STRING, self.current_literal)
                self.add_tokens(T_PLUS, self.current_char)
            elif self.current_char == T_MINUS:
                self.add_tokens(T_STRING, self.current_literal)
                self.add_tokens(T_MINUS, self.current_char)
            elif self.current_char == T_DIVISION:
                self.add_tokens(T_STRING, self.current_literal)
                self.add_tokens(T_DIVISION, self.current_char)
            elif self.current_char == T_MULTIPLY:
                self.add_tokens(T_STRING, self.current_literal)
                self.add_tokens(T_MULTIPLY, self.current_char)
            elif self.current_char == LPAREN:
                self.add_tokens(T_STRING, self.current_literal)
                self.add_tokens(LPAREN, self.current_char)
            elif self.current_char == RPAREN:
                self.add_tokens(T_STRING, self.current_literal)
                self.add_tokens(RPAREN, self.current_char)
            else: 
                self.current_literal += self.current_char
            self.next_char()
        
        self.pos = 0
        if len(self.current_literal) > 0:
            self.add_tokens(T_STRING, self.current_literal)

        if len(self.tokens) == 0:
            print(f"Current token '{self.current_literal}' is not defined.")
            return []
        else:
            to_return_tokens = self.tokens
            self.tokens = []
            return to_return_tokens

    def add_tokens(self, _type : str, value : str) -> None:
        """
        1. Create an instance of Token class with right type.
        2. Add an instance of Token class to self.tokens.
        """
        if _type == T_STRING and value != "":
            if value.isdigit():
                self.tokens.append(Token(T_NUMBER, int(value)))
            else:
                try:
                    self.tokens.append(Token(T_NUMBER, float(value)))
                except:
                    self.tokens.append(Token(T_STRING, value))
        elif value != "":
            self.tokens.append(Token(_type, value))
        self.current_literal = ""
from typing import List, Tuple
from lexer_token import Token
from variables import Variables

class Lexer(Variables):
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
        self.variable_complete = None
        while self.current_char != None:
            if self.current_char == self.T_PLUS:
                self.add_tokens(self.T_STRING, self.current_literal)
                self.add_tokens(self.T_PLUS, self.current_char)
            elif self.current_char == self.T_MINUS:
                self.add_tokens(self.T_STRING, self.current_literal)
                self.add_tokens(self.T_MINUS, self.current_char)
            elif self.current_char == self.T_DIVISION:
                self.add_tokens(self.T_STRING, self.current_literal)
                self.add_tokens(self.T_DIVISION, self.current_char)
            elif self.current_char == self.T_MULTIPLY:
                self.add_tokens(self.T_STRING, self.current_literal)
                self.add_tokens(self.T_MULTIPLY, self.current_char)
            elif self.current_char == self.LPAREN:
                self.add_tokens(self.T_STRING, self.current_literal)
                self.add_tokens(self.LPAREN, self.current_char)
            elif self.current_char == self.RPAREN:
                self.add_tokens(self.T_STRING, self.current_literal)
                self.add_tokens(self.RPAREN, self.current_char)
            elif self.current_char == self.T_EQUALS:
                self.add_tokens(self.T_VARIABLE, self.current_literal)
            else: 
                self.current_literal += self.current_char
            self.next_char()
        
        self.pos = 0
        if len(self.current_literal) > 0:
            self.add_tokens(self.T_STRING, self.current_literal)

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
        if _type == self.T_VARIABLE:
            self.tokens.append(Token(_type, None, value))
            self.variable_complete = False
        elif self.variable_complete == False:
            print("asd")
            is_number, new_value = self.transfrom_input(value)
            if is_number:
                print("asdas")
                self.tokens[-1].value = new_value
            else:
                self.tokens[-1].value = value
            self.variable_complete = True
        elif _type == self.T_STRING and value != "":
            is_number, new_value = self.transfrom_input(value)
            if is_number:
                self.tokens.append(Token(self.T_NUMBER, new_value))
            else:
                self.tokens.append(Token(self.T_NUMBER, new_value))
        elif value != "":
            self.tokens.append(Token(_type, value))
        self.current_literal = ""

    def transfrom_input(self, value):
        """
        Check if input is int or float and transfrom it.
        """
        is_number = False
        new_value = 0
        if value.isdigit():
            is_number == True
            new_value = int(value)
        else:
            try:
                new_value = float(value)
                is_number = True
            except:
                pass
        return is_number, new_value
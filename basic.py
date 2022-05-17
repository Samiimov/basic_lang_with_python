from lexer import Lexer
from ast_parser import Parser

class BasicLang:
    def __init__(self) -> None:
        self.lexer = Lexer()
        self.tokens = [] # List of tuples

    def handle_input(self, input):
        self.tokens = self.lexer.tokenize(input)
        print(self.tokens)
        self.parser = Parser(self.tokens)
        self.ast = self.parser.parse()
        print(self.ast)
        #self.parser.show_tree()

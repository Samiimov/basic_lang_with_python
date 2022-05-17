from lexer import Lexer
from ast_parser import Parser
from intepreter import Interpreter
class BasicLang:
    DONT_PRINT_LIST = [None, ""]    
    def __init__(self) -> None:
        self.lexer = Lexer()
        self.parser = Parser()
        self.interpreter = Interpreter()
        self.tokens = [] # List of tuples

    def handle_input(self, input):
        self.tokens = self.lexer.tokenize(input)
        self.ast = self.parser.parse(self.tokens)
        print(self.tokens)
        self.parser.show_tree()
        result = self.interpreter.interpret(self.ast)
        if not result in self.DONT_PRINT_LIST:
            print(result)

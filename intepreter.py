from ast_parser import BinOp, Num, Str
from variables import Variables
class Interpreter(Variables):
    def __init__(self) -> None:
        self.variables = []

    def interpret(self, node : BinOp):
        return self.generic_visit(node)

    def generic_visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name) # Return self.visit_BinOp method
        return visitor(node)

    def visit_BinOp(self, node : BinOp):
        if node.op.type == "+":
            return self.generic_visit(node.left) + self.generic_visit(node.right) 
        elif node.op.type == "-":
            return self.generic_visit(node.left) - self.generic_visit(node.right)   
        elif node.op.type == "*":
            return self.generic_visit(node.left) * self.generic_visit(node.right)
        elif node.op.type == "/":
            return self.generic_visit(node.left) / self.generic_visit(node.right)
    
    def visit_Num(self, node : Num):
        return node.value

    def visit_String(self, node : Str):
        return node.value

    def visit_Variable(self, node : Str):
        self.variables.append(node)
        return None
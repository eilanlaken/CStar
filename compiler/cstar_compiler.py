from compiler.lexer.lexer import Lexer
from compiler.parser.parser import Parser


class CStarCompiler:

    def __init__(self):
        self.lexer_instance = Lexer()
        self.parser_instance = Parser()

    def compile_program(self, program):
        pass

    def compile_file(self, file):
        pass

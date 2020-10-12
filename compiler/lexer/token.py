from compiler.lexer.token_types import *
import re


class Token:

    def __init__(self, token_type, match):
        self.token_type = token_type
        self.match = match

    def print(self):
        print("<" + self.token_type.name + ' , ' + self.match + ">")

    def print_verbose(self):
        print('<' + self.token_type + ' , ' + self.match + '>')

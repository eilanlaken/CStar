from typing import Any, Tuple, Union

from compiler.lexer.token_types import TokenType as TokenType

all_token_types = [t for t in TokenType]


class Token:

    def __init__(self, token_type, match):
        self.token_type = token_type
        self.match = match

    def print(self):
        print("<" + self.token_type.name + ' , ' + self.match + ">")

    def print_verbose(self):
        print('<' + self.token_type + ' , ' + self.match + '>')


def tokenize_code(code):
    code_length = len(code)
    tokens_stream = []
    i = 0
    while i < code_length:
        token = _find_next(code, i)
        tokens_stream.append(token)
        if token is not None:
            i += token[1].end()
            print(token)
        else:
            i += 1
            print('None')
    return tokens_stream


def _find_next(code, i):
    found_token = None
    for j in range(i, len(code)):
        current_str = code[i:j]
        for t in all_token_types:
            match = t.value[1].match(current_str)
            if match is None:
                continue
            else:
                found_token = (t, match)
    return found_token




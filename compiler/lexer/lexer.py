from typing import Any, Tuple, Union
from compiler.lexer.token_types import TokenType as TokenType
import re

all_token_types = [t for t in TokenType]


class Token:

    def __init__(self, token_type, match):
        self.token_type = token_type
        self.match = match

    def print(self):
        print("<" + self.token_type.name + ' , ' + self.match + ">")

    def print_verbose(self):
        print('<' + self.token_type + ' , ' + self.match + '>')


class Lexer:

    def __init__(self):
        self.current_tokens = []

    def tokenize_code(self, code):
        self.current_tokens = _tokenize_str(code)


def _tokenize_str(code):
    code_length = len(code)
    tokens_stream = []
    i = 0
    while i < code_length:
        token = __find_next__(code, i)
        tokens_stream.append(token)
        if token is not None:
            i += token[1].end()
        else:
            i += 1
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


def __find_next__(code, i):
    found_tokens = []
    current_str = code[i:len(code)]
    for t in all_token_types:
        match = t.value[1].match(current_str)
        if match is None:
            pass
        else:
            found_tokens.append((t, match, match.end()))
    longest_match = max(found_tokens, key=lambda k: k[2])
    return longest_match[0], longest_match[1], i, i + longest_match[1].end()


def omit_insignificant_tokens(tokens):
    filtered = []
    for token in tokens:
        if token is not None:
            token_type: TokenType = token[0]
            if token_type == TokenType.WhiteSpace or token_type == TokenType.Tab:
                pass
            else:
                filtered.append(token)
    return filtered



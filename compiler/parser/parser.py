

class Parser:

    def __init__(self):
        self.concrete_syntax_tree = None
        self.symbols_table = SymbolsTable()

    def generate_concrete_syntax_tree(self, token_stream):
        pass

    def generate_symbols_table(self, concrete_syntax_tree):
        pass


class SymbolsTable:

    def __init__(self):
        pass
class SymbolsTable:
    def __init__(self):
        self._symbols = []

    def get(self):
        return self._symbols

    def insert(self, item):
        if item not in self._symbols:
            self._symbols.append(item)

    def search(self, lexeme):
        for item in self._symbols:
            if item.lexeme == lexeme:
                return item

        return None

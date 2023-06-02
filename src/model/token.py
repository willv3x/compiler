class Token:
    def __init__(self, token_class, lexeme, token_type):
        self.token_class = token_class
        self.lexeme = lexeme
        self.token_type = token_type

    def __repr__(self):
        return 'Class: {}, Lexeme: {}, Type: {}'\
            .format(repr(self.token_class), repr(self.lexeme), repr(self.token_type))

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.token_class == other.token_class and self.lexeme == other.lexeme
        return NotImplemented

    def __ne__(self, other):
        x = self.__eq__(other)
        if x is not NotImplemented:
            return not x
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

class SyntacticError(Exception):
    def __init__(self, error):
        self.message = error

    def __repr__(self):
        return '{}'.format(repr(self.message))

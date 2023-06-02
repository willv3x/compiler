from src.model.deterministic_finite_automaton import DeterministicFiniteAutomaton
from src.model.lexical_error import LexicalError
from src.model.language import STATES, LETTERS, NUMBERS, SYMBOLS, INITIAL_STATE, FINAL_STATES, TRANSITION, WORDS
from src.model.token import Token


def _find_reserved_words(token) -> Token:
    if token.token_class == 'id' and token.lexeme in WORDS:
        return Token(token.lexeme, token.lexeme, token.lexeme)

    return token


class LexicalAnalyzer:
    def __init__(self, source_file, symbols_table):
        self._source_file = source_file
        self._automaton = DeterministicFiniteAutomaton(
            STATES,
            LETTERS + NUMBERS + SYMBOLS,
            INITIAL_STATE,
            FINAL_STATES,
            TRANSITION
        )
        self._line = 1
        self._column = 0
        self.errors = []

        self._symbols_table = symbols_table
        for _word in WORDS:
            self._symbols_table.insert(Token(_word, _word, _word))

    def scan(self) -> (Token, int, int):

        token = self._next()

        token = _find_reserved_words(token)

        self._update_symbols_table(token)

        # print(token)

        return token, self._line, self._column

    def _next(self) -> Token:
        while True:
            character = self._source_file.read(1)

            token = self._automaton.read(character)

            self._update_read_data(character)

            if token is not None and token.token_class == 'ERRO':
                self._handle_lexical_error(token)

            if token is not None and token.token_class != 'Ignorar' and token.token_class != 'Comentário' \
                    and token.token_class != 'ERRO':
                break

        return token

    def _handle_lexical_error(self, token):
        lexical_error = LexicalError('Lexical ERROR – line {}, column {}: {}'
                                     .format(repr(self._line), repr(self._column), repr(token.lexeme)))

        print(lexical_error)
        self.errors.append(lexical_error)

    def _update_symbols_table(self, token):
        if token.token_class == 'id':
            self._symbols_table.insert(Token(token.token_class, token.lexeme, token.token_type))

    def _update_read_data(self, character):
        if character == '\n':
            self._line += 1
            self._column = 0
        else:
            self._column += 1

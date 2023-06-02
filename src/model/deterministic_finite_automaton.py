from src.model.token import Token


class DeterministicFiniteAutomaton:
    def __init__(self, states, symbols, initial_state, final_state, transition):
        self._states = states
        self._symbols = symbols
        self._initial_state = initial_state
        self._final_state = final_state
        self._transition = transition

        self._state = self._initial_state
        self._lexeme = ''

    def read(self, character) -> Token:

        if not self._symbols.__contains__(character):
            token = Token('ERROR', character, None)
            self._state = self._initial_state
            self._lexeme = ''
            return token

        if self._state is None or self._transition[self._state].get(character) is None:
            token = self.finish()
        else:
            token = None

        self.transiciona(character)
        return token

    def finish(self) -> Token:
        if self._state in self._final_state:
            token = self._final_state[self._state]
            token.lexema = self._lexeme

            self._state = self._initial_state
            self._lexeme = ''

            return token
        else:
            token = Token('ERRO', self._lexeme, None)
            self._state = self._initial_state
            self._lexeme = ''
            return token

    def transiciona(self, caractere):
        self._lexeme += caractere
        self._state = self._transition[self._state].get(caractere)

import os
import pandas as pd

from src.model.syntactic_error import SyntacticError
from src.model.stack import Stack
from src.model.language import CONTEXT_FREE_GRAMMAR


def _csv_to_dict(path):
    result = pd.read_csv(os.path.join(os.path.dirname(__file__), path), sep=';', encoding="utf-8")
    result = result.set_index('estado')
    result = result.where(pd.notnull(result), None)
    result = result.T.to_dict()
    return result


class SyntacticAnalyzer:
    def __init__(self, lexical_analyzer, semantic_analyzer):
        self._lexical_analyzer = lexical_analyzer
        self._semantic_analyzer = semantic_analyzer
        self._syntactic_stack = Stack(initial_element=0)
        self._actionDict = _csv_to_dict('files/action.csv')
        self._gotoDict = _csv_to_dict('files/goto.csv')
        self.errors = []

    def parse(self):
        a, line, column = self._lexical_analyzer.scan()
        while True:
            s = self._syntactic_stack.top()
            action = self._action(s, a)

            if action[0] == 'S':
                t = int(action[1:])
                self._syntactic_stack.stack_up(t)  # Syntactic stack
                self._semantic_analyzer.stack_up(a)  # Semantic stack
                a, line, column = self._lexical_analyzer.scan()

            elif action[0] == 'R':
                action_number = int(action[1:]) + 1
                A, B = CONTEXT_FREE_GRAMMAR[action_number]

                self._syntactic_stack.unstack(len(B))
                t = self._syntactic_stack.top()

                goto = self._goto(t, A)
                self._syntactic_stack.stack_up(goto)

                print(f'{A} -> {" ".join(B)}')
                self._semantic_analyzer.analyze(action_number, line, column)

            elif action == 'ACC' or a.token_class.lower() == 'eof':
                break

            else:
                a, line, column = self._panic_mode_error_recovery(a, line, column, action)

    def _panic_mode_error_recovery(self, token, line, column, action):
        syntactic_error = SyntacticError(
            'Syntactic ERROR - line {}, column {}: {} ({})'
            .format(repr(line), repr(column), repr(token.lexeme), repr(action)))

        print(syntactic_error)
        self.errors.append(syntactic_error)

        while True:
            a, line, column = self._lexical_analyzer.scan()

            if a.token_class.lower() == 'pt_v' or a.token_class.lower() == 'eof':
                break

        return a, line, column

    def _action(self, s, a):
        return self._actionDict[s].get(a.token_class.lower())

    def _goto(self, t, a):
        return int(self._gotoDict[t].get(a))

from src.model.semantic_error import SemanticError
from src.model.stack import Stack
from src.model.language import CONTEXT_FREE_GRAMMAR
from src.model.token import Token


class SemanticAnalyzer:
    def __init__(self, symbols_table):
        self._symbols_table = symbols_table
        self._semantic_stack = Stack()
        self._line = 1
        self._column = 0
        self._temporary_variables = []
        self.errors = []
        self.code = ''

    def stack_up(self, a):
        self._semantic_stack.stack_up(Token(a.token_class.lower(), a.lexeme, a.token_type))

    def analyze(self, rule_number, line, column):
        self._line = line
        self._column = column

        left, right = CONTEXT_FREE_GRAMMAR[rule_number]
        unstacked = self._semantic_stack.unstack(len(right))

        if rule_number == 1:
            self._semantic_stack.stack_up(self._rule1(left, right, unstacked))
            return
        elif rule_number == 2:
            self._semantic_stack.stack_up(self._rule2(left, right, unstacked))
            return
        elif rule_number == 3:
            self._semantic_stack.stack_up(self._rule3(left, right, unstacked))
            return
        elif rule_number == 4:
            self._semantic_stack.stack_up(self._rule4(left, right, unstacked))
            return
        elif rule_number == 5:
            self._semantic_stack.stack_up(self._rule5(left, right, unstacked))
            return
        elif rule_number == 6:
            self._semantic_stack.stack_up(self._rule6(left, right, unstacked))
            return
        elif rule_number == 7:
            self._semantic_stack.stack_up(self._rule7(left, right, unstacked))
            return
        elif rule_number == 8:
            self._semantic_stack.stack_up(self._rule8(left, right, unstacked))
            return
        elif rule_number == 9:
            self._semantic_stack.stack_up(self._rule9(left, right, unstacked))
            return
        elif rule_number == 10:
            self._semantic_stack.stack_up(self._rule10(left, right, unstacked))
            return
        elif rule_number == 11:
            self._semantic_stack.stack_up(self._rule11(left, right, unstacked))
            return
        elif rule_number == 12:
            self._semantic_stack.stack_up(self._rule12(left, right, unstacked))
            return
        elif rule_number == 13:
            self._semantic_stack.stack_up(self._rule13(left, right, unstacked))
            return
        elif rule_number == 14:
            self._semantic_stack.stack_up(self._rule14(left, right, unstacked))
            return
        elif rule_number == 15:
            self._semantic_stack.stack_up(self._rule15(left, right, unstacked))
            return
        elif rule_number == 16:
            self._semantic_stack.stack_up(self._rule16(left, right, unstacked))
            return
        elif rule_number == 17:
            self._semantic_stack.stack_up(self._rule17(left, right, unstacked))
            return
        elif rule_number == 18:
            self._semantic_stack.stack_up(self._rule18(left, right, unstacked))
            return
        elif rule_number == 19:
            self._semantic_stack.stack_up(self._rule19(left, right, unstacked))
            return
        elif rule_number == 20:
            self._semantic_stack.stack_up(self._rule20(left, right, unstacked))
            return
        elif rule_number == 21:
            self._semantic_stack.stack_up(self._rule21(left, right, unstacked))
            return
        elif rule_number == 22:
            self._semantic_stack.stack_up(self._rule22(left, right, unstacked))
            return
        elif rule_number == 23:
            self._semantic_stack.stack_up(self._rule23(left, right, unstacked))
            return
        elif rule_number == 24:
            self._semantic_stack.stack_up(self._rule24(left, right, unstacked))
            return
        elif rule_number == 25:
            self._semantic_stack.stack_up(self._rule25(left, right, unstacked))
            return
        elif rule_number == 26:
            self._semantic_stack.stack_up(self._rule26(left, right, unstacked))
            return
        elif rule_number == 27:
            self._semantic_stack.stack_up(self._rule27(left, right, unstacked))
            return
        elif rule_number == 28:
            self._semantic_stack.stack_up(self._rule28(left, right, unstacked))
            return
        elif rule_number == 29:
            self._semantic_stack.stack_up(self._rule29(left, right, unstacked))
            return
        elif rule_number == 30:
            self._semantic_stack.stack_up(self._rule30(left, right, unstacked))
            return
        elif rule_number == 31:
            self._semantic_stack.stack_up(self._rule31(left, right, unstacked))
            return
        elif rule_number == 32:
            self._semantic_stack.stack_up(self._rule32(left, right, unstacked))
            return

    def _rule1(self, left, right, unstacked):  # P' -> P
        return Token(left, None, None)

    def _rule2(self, left, right, unstacked):  # P -> inicio V A
        return Token(left, None, None)

    def _rule3(self, left, right, unstacked):  # V -> varinicio LV
        return Token(left, None, None)

    def _rule4(self, left, right, unstacked):  # LV -> D LV
        return Token(left, None, None)

    def _rule5(self, left, right, unstacked):  # LV -> varfim pt_v
        # self.codigo += '\n\n\n'
        return Token(left, None, None)

    def _rule6(self, left, right, unstacked):  # D -> TIPO L pt_v
        TIPO = unstacked[2]
        L = unstacked[1]
        pt_v = unstacked[0]

        L.tipo = TIPO.token_type  # ??

        for id in L.lexeme.split(','):
            self.code += f'{TIPO.token_type} {id}{pt_v.lexeme}\n'

        return Token(left, None, TIPO.tipo)

    def _rule7(self, left, right, unstacked):  # L -> id vir L
        id = unstacked[2]
        vir = unstacked[1]
        L = unstacked[0]

        TIPO = self._semantic_stack.get_first_match('TIPO')

        symbol = self._symbols_table.search(id.lexema)
        symbol.token_type = TIPO.token_type

        return Token(left, f'{id.lexeme},{L.lexeme}', TIPO.token_type)

    def _rule8(self, left, right, unstacked):  # L -> id
        id = unstacked[0]

        TIPO = self._semantic_stack.get_first_match('TIPO')

        symbol = self._symbols_table.buscar(id.lexema)
        symbol.token_type = TIPO.token_type

        # self.code += f'{id.lexeme}'
        return Token(left, id.lexeme, TIPO.token_type)

    def _rule9(self, left, right, unstacked):  # TIPO -> inteiro
        integer = unstacked[0]
        return Token(left, integer.lexeme, integer.token_type)

    def _rule10(self, left, right, unstacked):  # TIPO -> real
        real = unstacked[0]
        return Token(left, real.lexeme, real.token_type)

    def _rule11(self, left, right, unstacked):  # TIPO -> literal
        literal = unstacked[0]
        return Token(left, literal.lexeme, literal.token_type)

    def _rule12(self, left, right, unstacked):  # A -> ES A
        return Token(left, None, None)

    def _rule13(self, left, right, unstacked):  # ES -> leia id pt_v
        id = unstacked[1]

        symbol = self._symbols_table.buscar(id.lexema)

        if symbol is not None and symbol.token_type is not None:
            if symbol.token_type == 'literal':
                self.code += f'scanf("%s", {id.lexeme});\n'
            if symbol.token_type == 'inteiro':
                self.code += f'scanf("%d", &{id.lexeme});\n'
            if symbol.token_type == 'real':
                self.code += f'scanf("%f", &{id.lexeme});\n'
        else:
            semantic_error = SemanticError('Semantic ERROR - line {}, column {}.'
                                           .format(repr(self._line), repr(self._column)))

            self._handle_semantic_error(semantic_error)

        return Token(left, None, None)

    def _rule14(self, left, right, unstacked):  # ES -> escreva ARG pt_v
        ARG = unstacked[1]
        self.code += f'printf({ARG.lexeme});\n'
        return Token(left, None, None)

    def _rule15(self, left, right, unstacked):  # ARG -> lit
        lit = unstacked[0]
        return Token(left, lit.lexeme, lit.token_type)

    def _rule16(self, left, right, unstacked):  # ARG -> num
        num = unstacked[0]
        return Token(left, num.lexeme, num.token_type)

    def _rule17(self, left, right, unstacked):  # ARG -> id
        id = unstacked[0]

        symbol = self._symbols_table.search(id.lexeme)

        ARG = Token(left, id.lexeme, id.token_type)

        if symbol is not None and symbol.token_type is not None:
            ARG = Token(left, symbol.lexeme, symbol.token_type)
        else:
            semantic_error = SemanticError('Semantic ERROR - line {}, column {}.'
                                           .format(repr(self._line), repr(self._column)))

            self._handle_semantic_error(semantic_error)

        return ARG

    def _rule18(self, left, right, unstacked):  # A -> CMD A
        return Token(left, None, None)

    def _rule19(self, left, right, unstacked):  # CMD -> id atr LD pt_v
        id = unstacked[3]
        LD = unstacked[1]

        symbol = self._symbols_table.search(id.lexeme)
        if symbol is not None and symbol.token_type is not None:
            if LD.token_type == symbol.token_type:
                self.code += f'{id.lexeme}={LD.lexeme};\n'
            else:
                semantic_error = SemanticError('Semantic ERROR - line {}, column {}.'
                                               .format(repr(self._line), repr(self._column)))

                self._handle_semantic_error(semantic_error)
        else:
            semantic_error = SemanticError('Semantic ERROR - line {}, column {}.'
                                           .format(repr(self._line), repr(self._column)))

            self._handle_semantic_error(semantic_error)

        return Token(left, None, None)

    def _rule20(self, left, right, unstacked):  # LD -> OPRD opa OPRD
        OPRD = unstacked[2]
        opa = unstacked[1]
        OPRD1 = unstacked[0]

        LD = Token(left, None, None)

        if OPRD.token_type != 'literal' and OPRD1.token_type == OPRD.token_type:
            LD.token_type = OPRD.token_type

            temporary_variable = len(self._temporary_variables)
            self.code += f'T{temporary_variable}={OPRD.lexeme}{opa.lexeme}{OPRD1.lexeme};\n'
            self._temporary_variables.append(LD.token_type)

            LD.lexeme = f'T{temporary_variable}'

        else:
            semantic_error = SemanticError('Semantic ERROR - line {}, column {}.'
                                           .format(repr(self._line), repr(self._column)))

            self._handle_semantic_error(semantic_error)

        return LD

    def _rule21(self, left, right, unstacked):  # LD -> OPRD
        OPRD = unstacked[0]
        return Token(left, OPRD.lexeme, OPRD.token_type)

    def _rule22(self, left, right, unstacked):  # OPRD -> id
        id = unstacked[0]

        symbol = self._symbols_table.search(id.lexeme)

        OPRD = Token(left, id.lexeme, None)
        if symbol is not None and symbol.token_type is not None:
            OPRD.token_type = symbol.token_type
        else:
            semantic_error = SemanticError('Semantic ERROR - line {}, column {}.'
                                           .format(repr(self._line), repr(self._column)))

            self._handle_semantic_error(semantic_error)

        return OPRD

    def _rule23(self, left, right, unstacked):  # OPRD -> num
        num = unstacked[0]
        return Token(left, num.lexeme, num.token_type)

    def _rule24(self, left, right, unstacked):  # A -> COND A
        return Token(left, None, None)

    def _rule25(self, left, right, unstacked):  # COND -> CAB CP
        self.code += '}\n'
        return Token(left, None, None)

    def _rule26(self, left, right, unstacked):  # CAB -> se ab_p EXP_R fc_p entao
        EXP_R = unstacked[2]
        self.code += f'if({EXP_R.lexeme})''\n{\n'
        return Token(left, None, None)

    def _rule27(self, left, right, unstacked):  # EXP_R -> OPRD opr OPRD
        OPRD = unstacked[2]
        opr = unstacked[1]
        OPRD1 = unstacked[0]

        temporary_variable = len(self._temporary_variables)
        self.code += f'T{temporary_variable}={OPRD.lexeme}{opr.lexeme}{OPRD1.lexeme};\n'
        self._temporary_variables.append('inteiro')

        return Token(left, f'T{temporary_variable}', None)

    def _rule28(self, left, right, unstacked):  # CP -> ES CP
        return Token(left, None, None)

    def _rule29(self, left, right, unstacked):  # CP -> CMD CP
        return Token(left, None, None)

    def _rule30(self, left, right, unstacked):  # CP -> COND CP
        return Token(left, None, None)

    def _rule31(self, left, right, unstacked):  # CP -> fimse
        return Token(left, None, None)

    def _rule32(self, left, right, unstacked):  # A -> fim
        return Token(left, None, None)

    def _handle_semantic_error(self, semantic_error):
        print(semantic_error)
        self.errors.append(semantic_error)

    def _generate_temporary_variables(self):
        temporary_variables = ''
        temporary_variables += '/*-------Variáveis temporárias----------*/\n'
        for i, T in enumerate(self._temporary_variables):
            temporary_variables += f'{T} T{i};\n'
        temporary_variables += '/*--------------------------------------*/\n'

        return temporary_variables

    def generate(self, target_file):
        start = '#include <stdio.h>\ntypedef char literal[256];\nvoid main(void)\n{\n'
        temporary_variables = self._generate_temporary_variables()

        final_code = start + temporary_variables + self.code + '}'

        final_code = final_code.replace('inteiro', 'int')
        final_code = final_code.replace('real', 'double')

        # print(final_code)

        target_file.write(final_code)




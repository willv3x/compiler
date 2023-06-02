import os

from src.lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from src.semantic_analyzer.semantic_analyzer import SemanticAnalyzer
from src.syntactic_analyzer.syntactic_analyzer import SyntacticAnalyzer
from src.model.symbols_table import SymbolsTable


def main():
    symbols_table = SymbolsTable()

    path_source_file = os.path.join(os.path.dirname(__file__), '../SOURCE.ALG')
    source_file = open(path_source_file, mode='r', encoding='utf-8')

    scanner = LexicalAnalyzer(source_file, symbols_table)
    generator = SemanticAnalyzer(symbols_table)
    parser = SyntacticAnalyzer(scanner, generator)

    parser.parse()

    source_file.close()

    path_target_file = os.path.join(os.path.dirname(__file__), '../PROGRAM.C')
    target_file = open(path_target_file, mode='w', encoding='utf-8')

    if scanner.errors.__len__() == 0 and parser.errors.__len__() == 0 and generator.errors.__len__() == 0:
        generator.generate(target_file)

    target_file.close()

    # print('\n============================== Symbols =================================\n')
    # for symbol in symbols_table.get():
    #     print(symbol)


main()

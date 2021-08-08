from pathlib import Path

from lark import Lark

HERE = Path(__file__).parent
grammar_file = HERE.joinpath("grammar.lark")

parser = Lark(grammar_file.read_text(), parser="lalr")


def parse_file(filename):
    return parser.parse(open(filename).read())

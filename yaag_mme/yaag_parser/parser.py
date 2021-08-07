from pathlib import Path

from lark import Lark

HERE = Path(__file__).parent
grammar_file = HERE.joinpath("grammar.lark")

parser = Lark(grammar_file.read_text(), parser="lalr")

import re

from yaag_mme.yaag_parser.token import Token
from yaag_mme.yaag_parser.token_type import TokenType


class Lexer:
    _patterns = [
        (r"^\[[a-zA-Z]+\s?(?<=\s).*\]$", TokenType.COMMAND),
        (r"(    )+.+", TokenType.PARAMETER)
    ]

    @staticmethod
    def tokenize(string: str):
        tokens = []

        split_string = string.split("\n")

        for line in split_string:
            for pattern, type_ in Lexer._patterns:
                if re.search(pattern, line):
                    tokens.append(Token(type_, line))

        return tokens

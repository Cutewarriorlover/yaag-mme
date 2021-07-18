import re

from yaag_mme.yaag_parser.token import Token
from yaag_mme.yaag_parser.token_type import TokenType


class Lexer:
    _patterns = {
        "command": r"\[[a-zA-Z]+\s?(?<=\s).*\]"
    }

    @staticmethod
    def tokenize(string: str):
        tokens = []

        split_string = string.split("\n")

        for line in split_string:
            if re.match(Lexer._patterns["command"], line):
                tokens.append(Token(TokenType.COMMAND, line))

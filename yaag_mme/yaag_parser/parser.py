import re

from yaag_mme.yaag_parser.command import Command
from yaag_mme.yaag_parser.parameter import Parameter
from yaag_mme.yaag_parser.token_type import TokenType


class Parser:
    _patterns = {
        "command": r"^\[([a-zA-Z]+)\s?(?<=\s)(.*)\]$",
        "parameter": r"((    )+)(.+)"  # File regex: (\[(([a-zA-Z\-_.]\/?)+\.yaag)\])?
    }

    @staticmethod
    def parse(tokens):
        parsed = []

        for token in tokens:
            if token.type_ == TokenType.COMMAND:
                match = re.search(Parser._patterns["command"], token.value)

                command = Command(match.group(1), match.group(2))
                parsed.append(command)
            elif token.type_ == TokenType.PARAMETER:
                match = re.search(Parser._patterns["parameter"], token.value)

                parameter = Parameter(match.group(3))
                parsed.append(parameter)
        return parsed

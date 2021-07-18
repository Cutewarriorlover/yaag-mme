from enum import Enum, auto


class TokenType(Enum):
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()

    COMMAND = auto()
    SPECIAL_PARAMETER = auto()
    PARAMETER = auto()

import re


def is_blank(string):
    """
    This function returns if the string is blanks or not.

    Args:
      string(str): The string to check.

    Returns:
      bool: Whether the string is blank
    """
    return re.match(r"^\s*$", string)


def lower_equals(string, match):
    """
    This function returns if ``string`` lowercase is equal to ``match``.

    Args:
      string(str): The string to check.
      match(str): The match to check against.

    Returns:
      bool: Whether ``string`` lowercase is equal to ``match``.
    """
    return string.lower() == match


def lower_in(string, matches):
    """
    This function returns if ``string`` lowercase is in ``matches``.

    Args:
      string(str): The string to check.
      matches(Iterable): The list of matches to check against.

    Returns:
      bool: Whether ``string`` lowercase is in ``matches``.
    """
    return string.lower() in matches

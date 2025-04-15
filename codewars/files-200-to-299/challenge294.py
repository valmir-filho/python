"""
Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a single digit (0-9), false otherwise.
"""


def is_digit(n):
    return isinstance(n, str) and len(n) == 1 and n.isdigit()

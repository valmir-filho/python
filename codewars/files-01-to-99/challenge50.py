"""
Check to see if a string has the same amount of "x"s and "o"s.
The method must return a boolean and be case insensitive.
The string can contain any char.
"""


def equal_x_and_o(string):
    string_lower = string.lower()
    count_x = string_lower.count('x')
    count_o = string_lower.count('o')
    return count_x == count_o

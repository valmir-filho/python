"""
Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language.
See the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase.

As usual, your function/method should be pure, i.e. it should not mutate the original string.
"""


def to_alternating_case(string):
    # List comprehension to swap case for each character.
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

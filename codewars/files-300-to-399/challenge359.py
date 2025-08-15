"""
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.
"""


def switcheroo(s):
    return s.translate(str.maketrans({'a': 'b', 'b': 'a'}))

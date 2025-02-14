"""
This function takes two numbers as parameters, the first number being the coefficient, and the second number being the exponent.

Your function should multiply the two numbers, and then subtract 1 from the exponent. Then, it has to return an expression (like 28x^7). "^1" should not be truncated when exponent = 2.

Notes:
- The output of this function should be a string.
- The exponent will never be 1, and neither number will ever be 0.
"""


def derive(coefficient, exponent):
    result = coefficient * exponent
    new_exponent = exponent - 1
    return f"{result}x^{new_exponent}"

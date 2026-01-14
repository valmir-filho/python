"""
Find the sum of the odd numbers within an array, after cubing the initial integers.
The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers.
"""


def cube_odd(arr):
    total = 0

    for x in arr:
        # rejeita não-inteiros e booleanos.
        if not isinstance(x, int) or isinstance(x, bool):
            return None

        cube = x ** 3
        if cube % 2 != 0:
            total += cube

    return total

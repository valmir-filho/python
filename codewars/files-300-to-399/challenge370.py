"""
Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

1st (1)   2nd (3)    3rd (6)
*          **        ***
           *         **
                     *

You need to return the nth triangular number. You should return 0 for out of range values.
"""


def triangular(n):
    # Verifica se o valor é positivo.
    if n <= 0:
        return 0
    # Fórmula do número triangular: n * (n + 1) / 2.
    return n * (n + 1) // 2
  

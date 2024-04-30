"""
Função "reduce()" no Python.

A função "reduce" está disponível no módulo "functools" no Python e é usada para reduzir uma sequência de valores a um único valor acumulado, aplicando uma função especificada.
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5]


def soma(x, y):
    return x + y


soma_total = reduce(soma, numeros)

print(soma_total)

"""
Neste exemplo, a função "soma" é aplicada iterativamente aos elementos da lista "numeros", reduzindo-a a um único valor. O resultado é a soma de todos os elementos na lista, que é 15.
"""

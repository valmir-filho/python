"""
Generator no Python.

Um gerador (generator) no Python é uma função especial que permite criar iteradores de maneira mais fácil e eficiente do que as abordagens tradicionais. Os geradores são úteis quando você precisa criar sequências de elementos, mas não deseja armazenar todos eles na memória de uma só vez. Em vez disso, os geradores produzem elementos sob demanda, economizando recursos.
"""

import sys

# lista = [number for number in range(1000000)]
# lista = [number for number in range(10000000)]
# print(lista)

# Usa-se parênteses para criar um generator
generator = (number for number in range(1000000))
# generator = (number for number in range(10000000))
# print(generator)

print(next(generator))
# print(next(generator))
# print(next(generator))

# print(sys.getsizeof(lista))
# print(sys.getsizeof(generator))

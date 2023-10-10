"""
Módulos imbutidos no Python.

O Python vem com uma variedade de módulos embutidos que oferecem funcionalidades prontas para uso. Alguns exemplos incluem "math", "random", "os", "datetime", entre outros. Você pode usar esses módulos diretamente em seus programas.

Documentação: https://docs.python.org/3/py-modindex.html

Observação: não é uma boa prática importar os módulos dessa forma: "from sys import *".
"""

# Importação do módulo inteiro
import math


def potencia(base, expoente):
    resultado = math.pow(base, expoente)
    return f"{base} elevado a {expoente} é {resultado:.0f}."


# print(potencia(2, 5))

# Importação de parte do módulo
# from math import sqrt


# def raiz_quadrada(numero):
#     resultado = sqrt(numero)
#     return f"A raiz quadrada de {numero} é {resultado:.0f}."


# print(raiz_quadrada(90))

# Importação do módulo por meio de um apelido (alias)
# import random as rnd

# numero_aleatorio = rnd.randint(1, 101)
# print(numero_aleatorio)

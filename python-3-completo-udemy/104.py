"""
Funções "map()", "filter()" e "reduce() aplicadas ao mesmo tempo no Python."
"""

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função para dobrar um número


def dobra(numero):
    return numero * 2

# Função para verificar se um número é par


def eh_par(numero):
    return numero % 2 == 0

# Função para somar dois números


def soma(x, y):
    return x + y


# Uso do "map" para dobrar cada número na lista
numeros_dobrados = list(map(dobra, numeros))

# Uso do "filter" para manter apenas os números pares
numeros_pares = list(filter(eh_par, numeros_dobrados))

# Uso do "reduce" para encontrar a soma dos números resultantes
soma_total = reduce(soma, numeros_pares)

print(soma_total)

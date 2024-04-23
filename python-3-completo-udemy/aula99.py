""" 
Função "itertools.groupby(iterable, key=None)".

A função "itertools.groupby(iterable, key=None)" recebe um iterável e uma função "key" opcional. Ela retorna um iterador que produz pares de chave/elemento, onde a chave é o resultado da função "key" aplicada a cada elemento do iterável e o elemento é um iterável que contém todos os elementos com a mesma chave.

Observação: para usar o "groupby", os dados precisam estar ordenados.
"""

from itertools import groupby

dados = [
    ("A", 1),
    ("B", 2),
    ("A", 3),
    ("C", 4),
    ("B", 5)
]

dados_ordenados = sorted(dados, key=lambda x: x[0])

grupos = groupby(dados_ordenados, key=lambda x: x[0])

for chave, grupo in grupos:
    print(f"Chave: {chave}")
    for elemento in grupo:
        print(elemento)

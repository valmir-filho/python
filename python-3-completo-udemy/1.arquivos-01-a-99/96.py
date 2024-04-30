"""
Exercício: considerando duas listas de números inteiros ou floats, some os valores, retornando o resultado em uma nova lista. Caso uma lista seja menor do que a outra, considere a menor delas.
"""

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [1, 2, 3, 4]

lista_3 = [a + b for a, b in zip(lista_1, lista_2)]
print(lista_3)

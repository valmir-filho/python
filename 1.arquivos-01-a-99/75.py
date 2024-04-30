"""
Filtro de dados em list comprehension.

A list comprehension permite que você aplique uma condição de filtro diretamente durante a criação da nova lista. A condição é especificada após a expressão que você está aplicando a cada elemento da sequência.
"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando List Comprehension para criar uma nova lista com números pares
numeros_pares = [x for x in numeros if x % 2 == 0]
print(numeros_pares)

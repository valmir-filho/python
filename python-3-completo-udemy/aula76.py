"""
List comprehension com mais de um loop for.

Você pode usar list comprehensions com mais de um loop for para criar listas que envolvem iterações aninhadas sobre múltiplas sequências. Isso é útil quando você precisa combinar elementos de duas ou mais sequências de maneira coordenada. A sintaxe básica envolve aninhar os loops for uns dentro dos outros.
"""

lista1 = [1, 2, 3]
lista2 = ['a', 'b']

combinacao_lista1_lista2 = [(x, y) for x in lista1 for y in lista2]
print(combinacao_lista1_lista2)

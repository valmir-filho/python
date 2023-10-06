"""
Conjuntos no Python (sets).

Um conjunto é uma coleção de elementos não ordenada e mutável que não permite elementos duplicados. Os conjuntos são implementados usando a classe set. Aqui estão algumas características importantes dos conjuntos em Python:

- Não permite elementos duplicados. Um conjunto não pode conter elementos duplicados. Se você tentar adicionar um elemento que já está presente no conjunto, ele não será adicionado novamente.
- Não são indexados. Os elementos em um conjunto não têm uma posição específica, portanto, você não pode acessá-los por índice como faria em uma lista ou tupla.
- Mutáveis. Os conjuntos são mutáveis, o que significa que você pode adicionar e remover elementos após a criação do conjunto. Entretando, só aceitam valores imutáveis.
"""

# Criando um conjunto
conjunto1 = set({3, 4, 5})
print(conjunto1)
print(type(conjunto1))

# Itera o valor
# conjunto2 = set("Valmir")
# print(conjunto2)
# Não itera o valor
# conjunto3 = {"Valmir"}
# print(conjunto3)

# Outra forma de criação
# Parece um dicionário, mas não tem chave, apenas valor
# conjunto4 = {3, 4, 5}
# print(conjunto4)
# print(type(conjunto4))

# Criando um conjunto vazio
# conjunto5 = set()
# print(type(conjunto5))
# Cuidado! Dessa forma não é possível a criação de um conjunto vazio, pois conflita com a criação de um dicionário vazio
# conjunto6 = {}
# print(type(conjunto6))

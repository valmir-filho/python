# Permutações, combinações e produtos cartesianos usando o "itertools" no Python.

from itertools import permutations, combinations, product

# Permutações
elementos = ["A", "B", "C"]
permutacoes = permutations(elementos, 2)

for permutacao in permutacoes:
    print(permutacao)

# Combinações
# elementos = ['A', 'B', 'C']
# combinacoes = combinations(elementos, 2)

# for combinacao in combinacoes:
#     print(combinacao)

# Produtos cartesianos
# cores = ['vermelho', 'verde']
# tamanhos = ['pequeno', 'grande']
# tipos = ['maçã', 'banana']
# produtos = product(cores, tamanhos, tipos)

# for produto in produtos:
#     print(produto)

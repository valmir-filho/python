# Unidade 04: Listas.
"""Exemplo de aplicação 8: Dada a matriz m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], efetue a soma de todos os seus elementos
e exiba o resultado."""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0
for i in range(3):
    for j in range(3):
        soma += m[i][j]
print()
print('A soma dos elementos da matriz m é igual a {}'.format(soma))

# Unidade 04: Listas.
"""Exercício de fixação 6: dado o vetor nums = [3, 11, 6, 32, 15, 22, 4, 10, 5], crie uma matriz 3x3 com os três maiores
elementos na primeira linha, os três elementos intermediários na segunda linha e os elementos menores na terceira
linha."""

nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
linha1 = []
linha3 = []
matriz = []
for _ in range(3):
    linha1.append(nums.pop(nums.index(max(nums))))
    linha1.sort()
for _ in range(3):
    linha3.append(nums.pop(nums.index(min(nums))))
    linha3.sort()
nums.sort()
matriz.append(linha1)
matriz.append(nums)
matriz.append(linha3)
print(matriz)

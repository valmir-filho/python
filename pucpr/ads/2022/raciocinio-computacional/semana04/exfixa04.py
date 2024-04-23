# Unidade 04: Listas.
"""Exercício de fixação 4: Crie um programa que efetue a soma de duas matrizes 3x3, sabendo que a soma desse tipo de
matriz é uma nova matriz 3x3, sendo cada elemento resultado da soma dos elementos das matrizes na mesma posição."""

matriz_a = []
matriz_b = []
matriz_soma = []
for i in range(3):
    matriz_a.append([])
    for _ in range(3):
        num = float(input('Informe o elemento da matriz A: '))
        matriz_a[i].append(num)
for i in range(3):
    matriz_b.append([])
    for _ in range(3):
        num = float(input('Informe o elemento da matriz B: '))
        matriz_b[i].append(num)
for i in range(3):
    matriz_soma.append([])
    for j in range(3):
        num = matriz_a[i][j] + matriz_b[i][j]
        matriz_soma[i].append(num)
print()
print('Matriz A: {}'.format(matriz_a))
print('Matriz B: {}'.format(matriz_b))
print()
print('Matriz Soma: {}'.format(matriz_soma))

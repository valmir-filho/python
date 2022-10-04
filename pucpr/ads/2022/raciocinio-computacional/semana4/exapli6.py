# Unidade 04: Listas.
"""Exemplo de aplicação 6: Solicite ao usuário que digite três coordenadas (x, y), armazenando-as numa matriz
bidimensional"""

import time

coordenadas = []
for i in range(3):
    x = int(input('\33[32mInsira um valor de x: '))
    y = int(input('Insira um valor de y: \33[m'))
    coordenadas.append([x, y])
print()
print('Construindo as matrizes...')
time.sleep(3)
print()
print('As matrizes ficaram da seguinte forma: ')
print()
print(coordenadas)

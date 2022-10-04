"""Crie um programa que gere uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre:
a) a soma de todos os valores pares digitados;
b) a soma dos valores da terceira coluna;
c) o maior valor da segunda linha."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_ter_coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l+1},{c+1}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print('†' * 49)
print(f'A soma de todos os valores pares digitados é: {soma_pares}.')
for l in range(0, 3):
    soma_ter_coluna += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é: {soma_ter_coluna}.')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da 2ª linha é: {maior}.')
print('†' * 49)

""""Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros termos de uma
Sequência de Fibonacci.
Exemplo: 0 → 1 → 1 → 2 → 3 → 5 → 8."""

termo_1 = 0
termo_2 = 1
print('≈' * 22)
print('Sequência de Fibonacci')
print('≈' * 22)
n = int(input('Quantos termos você quer mostrar? '))
print()
contador = 3
print('\33[34mOs {} primeiros termos são: {} → {}'.format(n, termo_1, termo_2), end='')
while contador <= n:
    termo_3 = termo_1 + termo_2
    print(' → {}'.format(termo_3), end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1
print(' → Fim!\33[m')

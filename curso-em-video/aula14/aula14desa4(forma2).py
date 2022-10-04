""""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5!=5*4*3*2*1 = 120."""

from math import factorial
n = int(input('Informe um número inteiro qualquer para calcular o seu Fatorial: '))
contador = n
print('{}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1
print(factorial(n))

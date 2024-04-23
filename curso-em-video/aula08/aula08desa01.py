# Crie um programa que leia um número real qualquer e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('Digite um número real qualquer: '))
print('A porção inteira do número {} é: {}'.format(num, trunc(num)))

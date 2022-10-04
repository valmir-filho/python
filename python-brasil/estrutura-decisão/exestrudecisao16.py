"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 16: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;"""

import math
print()
print('=' * 44)
print('Cálculo das raízes de uma equação do 2º grau')
print('=' * 44)
print()
a = int(input('\33[32mInforme o valor de a: '))
if a == 0:
    print()
    print('O valor de "a" não pode ser 0, pois não forma uma equação do 2º grau.')
else:
    b = int(input('Informe o valor de b: '))
    c = int(input('Informe o valor de c: \33[m'))
    delta = b**2-4*a*c
    print()
    print('O valor do Delta é: {}'.format(delta))
    print()
    if delta < 0:
        print('A equação não possui raízes reais.')
    elif delta == 0:
        print('A equação possui apenas 1 raiz real igual a : {}'.format(-b/2*a))
    else:
        print('A equação possui 2 raízes reais iguais a : {} e {}'.format((-b + math.sqrt(delta))/(2*a), (-b - math.sqrt(delta))/(2*a)))

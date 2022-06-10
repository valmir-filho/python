"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 1: Faça um Programa que peça dois números e imprima o maior deles."""

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
if num1 > num2:
    print('{} é maior que {}'.format(num1,num2))
elif num1 < num2:
    print('{} é maior que {}'.format(num2,num1))
else:
    print('O {} e o {} são iguais'.format(num1,num2))

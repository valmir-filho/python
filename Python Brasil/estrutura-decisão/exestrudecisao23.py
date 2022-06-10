"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 23: Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento."""

num = float(input('Digite um número qualquer: '))
if num == int(num):
    print('O {} é um número inteiro'.format(num))
else:
    print('O {} é um número decimal'.format(num))

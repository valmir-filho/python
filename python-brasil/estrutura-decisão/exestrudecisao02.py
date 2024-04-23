"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 2: Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."""

valor = float(input('Digite um número qualquer: '))
if valor > 0:
    print('O {} é um número positivo'.format(valor))
elif valor < 0:
    print('O {} é um número negativo'.format(valor))
else:
    print('Você digitou o número {}'.format(valor))

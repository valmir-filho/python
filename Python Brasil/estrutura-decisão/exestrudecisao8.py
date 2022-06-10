"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 8: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo
que a decisão é sempre pelo mais barato."""

print()
p1 = float(input('\33[32mInforme o valor do produto 1: R$'))
p2 = float(input('Informe o valor do produto 2: R$'))
p3 = float(input('Informe o valor do produto 3: R$\33[m'))
print()
if p1 == p2 and p1 == p3:
    print('Preços iguais!!! Você pode optar por qualquer um dos produtos.')
elif p1 < p2 and p1 < p3:
    print('Você deve comprar o produto 1.')
elif p2 < p3:
    print('Você deve comprar o produto 2.')
else:
    print('Você deve comprar o produto 3.')

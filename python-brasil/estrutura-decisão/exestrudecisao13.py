"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 13: Faça um Programa que leia um número e exiba o dia correspondente da semana. (1–Domingo, 2–Segunda, etc.),
se digitar outro valor deve aparecer valor inválido."""

num = int(input('Digite um número entre 1 e 7: '))
if num == 1:
    print('1-Domingo')
elif num == 2:
    print('2-Segunda')
elif num == 3:
    print('3-Terça')
elif num == 4:
    print('4-Quarta')
elif num == 5:
    print('5-Quinta')
elif num == 6:
    print('6-Sexta')
elif num == 7:
    print('7-Sábado')
else:
    print('Valor inválido!')

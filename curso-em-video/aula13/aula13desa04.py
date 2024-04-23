""""Faça um programa que mostre a tabuada de um número escolhido pelo usuário."""

n = int(input('Escolha um número inteiro qualquer: '))
print('Tabuada do {}.'.format(n))
for c in range(0,11):
    print('{} * {} = {}'.format(n, c, n*c))

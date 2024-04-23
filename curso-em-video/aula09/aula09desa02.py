# Faça um programa que leia o número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Exemplo: Digite o número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

num = int(input('Informe um número inteiro entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}, ele possui: '.format(num))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))

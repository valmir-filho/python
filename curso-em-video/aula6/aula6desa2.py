# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as possíveis informações
# sobre ele.

x = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(x)))
print('Só tem espaços? {}'.format(x.isspace()))
print('É um número? {}'.format(x.isnumeric()))
print('É alfabético? {}'.format(x.isalpha()))
print('É alfanumérico {}?'.format(x.isalnum()))
print('Está em maiúsculo(a)? {}'.format(x.isupper()))
print('Está em minúsculo(a)? {}'.format(x.islower()))

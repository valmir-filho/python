""""Faça um programa que leia um número qualquer e mostre o seu fatorial.
Exemplo: 5!=5*4*3*2*1 = 120."""

n = int(input('Informe um número inteiro qualquer para calcular o seu Fatorial: '))
contador = n
# Quando eu for iniciar uma soma ou subtração, sempre inicio com "0". Na multiplicação, tenho que começar com 1, pois se multiplicar por "0", o resultado é igual a "0".
f = 1
print('{}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f)

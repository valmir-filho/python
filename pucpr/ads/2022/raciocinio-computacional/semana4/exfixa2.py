# Unidade 04: Listas.
"""Exercício de fixação 2: Crie um programa que solicite ao usuário duas listas com cinco elementos cada e, como
resultado, crie uma terceira lista que intercale os elementos das anteriores."""

import time
print()
lista1 = []
lista2 = []
intercalada = []
for i in range(5):
    num1 = float(input('\33[32mInforme o ' + str(i + 1) + 'º número da Lista 1: '))
    lista1.append(num1)
print()
for i in range(5):
    num2 = float(input('Informe o ' + str(i + 1) + 'º número da Lista 2: '))
    lista2.append(num2)
print()
print('\33[mGerando as listas...')
time.sleep(3)
print()
print('\33[34mA Lista 1 é: {}'.format(lista1))
print('A Lista 2 é: {}\33[m'.format(lista2))
for i in range(5):
    intercalada.append(lista1[i])
    intercalada.append(lista2[i])
print()
print('Intercalando as duas listas...')
time.sleep(3)
print()
print('\33[34mA Lista intercalada é: {}\33[m'.format(intercalada))

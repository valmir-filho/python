# Unidade 04: Listas.
"""Exercício de aplicação 2: Elabore um programa que solicite ao usuário cinco números e exiba duas listas, uma de
números pares e outra de números ímpares."""

import time

pares = []
impares = []
print()
for i in range(5):
    numeros = int(input('\33[32mDigite um número inteiro: \33[m'))
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)
print()
print('Criando as listas...')
time.sleep(3)
print()
print('\33[34mOs números pares são: {}\33[m'.format(pares))
print('\33[31mOs números ímpares são: {}\33[m'.format(impares))

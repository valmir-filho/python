# Unidade 04: Listas.
"""Exercício de fixação 1: Crie um programa que solicite ao usuário seis números, calculando a média, e mostre uma
lista com os números iguais ou acima da média e uma lista com os números abaixo da média."""

import time
print()
numeros = []
acima_media = []
abaixo_media = []
for i in range(6):
    num = float(input('\33[32mInforme o ' + str(i + 1) + 'º número: \33[m'))
    numeros.append(num)
media = sum(numeros) / 6
print()
print('Calculando a média...')
time.sleep(3)
print()
print('\33[34mA média dos números informados é: {:.2f}\33[m'.format(media))
for num in numeros:
    if num >= media:
        acima_media.append(num)
    else:
        abaixo_media.append(num)
print()
print('Gerando as listas...')
time.sleep(3)
print()
print('\33[34mA lista de números acima da média é: {}'.format(acima_media))
print()
print('A lista de números abaixo da média é: {}\33[m'.format(abaixo_media))

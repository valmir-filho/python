"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função
vai sortear 5 números e vai colocá-los em uma lista e a segunda função vai mostrar a soma entre todos os valores
pares sorteados pela função anterior."""

import time
from random import randint
numeros = []


def sorteia():
    for i in range(1, 6):
        n = randint(1, 10)
        numeros.append(n)
    print('Sorteando 5 valores da lista:', end=' ')
    for n in numeros:
        print(f'{n}', end=' ')
        time.sleep(0.5)
    print('Pronto!')


def somapar():
    s = 0
    for n in numeros:
        if n % 2 == 0:
            s += n
    print(f'Somando os valores pares de {numeros}, temos: {s}.')


sorteia()
somapar()

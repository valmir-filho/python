"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. O seu
programa tem que analisar todos os valores e dizer qual deles é o maior."""

import time


def maior(* n):
    print('§' * 60)
    print('Analisando os valores passados...')
    time.sleep(1)
    print(f'Foram informados os seguintes valores: {n}.')
    print(f'Total de valores: {len(n)}.')
    print(f'O maior valor informado foi: {max(n)}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
print('§' * 60)

"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla."""

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os número gerados foram: {n}.')
print(f'O maior número da tupla é: {max(n)}.')
print(f'O menor número da tupla é: {min(n)}.')

# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = float(input('Digite um 1º número qualquer: '))
b = float(input('Digite um 2º número qualquer: '))
c = float(input('Digite um 3º número qualquer: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

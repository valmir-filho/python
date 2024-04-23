"""Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra;
b) Quantos produtos custam mais de R$1.000,00;
c) Qual é o nome do produto mais barato."""

total = maior_1000 = menor = contador = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Digite o preço do produto R$'))
    contador += 1
    total += preco
    if preco > 1000:
        maior_1000 += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando produtos (S=sim/N=não)? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi de R${total:.2f}.')
print(f'{maior_1000} produtos custam mais de R$1.000,00.')
print(f'O produto mais barato foi o(a) {barato} que custou R${menor:.2f}.')

"""Faça um programa que leia nome e peso da várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves."""

pessoas_1 = []
pessoas_2 = []
maior = menor = 0
while True:
    nome = str(input('Digite o nome da pessoa: ')).strip().upper()
    pessoas_1.append(nome)
    peso = float(input('Digite o peso da pessoa: '))
    pessoas_1.append(peso)
    if len(pessoas_2) == 0:
        maior = menor = pessoas_1[1]
    else:
        if pessoas_1[1] > maior:
            maior = pessoas_1[1]
        if pessoas_1[1] < menor:
            menor = pessoas_1[1]
    pessoas_2.append(pessoas_1[:])
    pessoas_1.clear()
    continuar = str(input('Deseja continuar cadastrando pessoas? (S=sim/N=não): ')).strip().upper()
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(pessoas_2)} pessoas.')
print('As pessoas mais pesadas são: ', end='')
for p in pessoas_2:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print('As pessoas mais leves são: ', end='')
for p in pessoas_2:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')

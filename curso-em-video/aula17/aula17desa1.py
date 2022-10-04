"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista."""

valores = list()
maior = menor = 0
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
            maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado é o {maior} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}...', end='')
print(f'\nO menor valor digitado é o {menor} nas posições ', end='')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}...', end='')

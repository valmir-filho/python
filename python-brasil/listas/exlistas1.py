"""Python Brasil
Lista de exercícios de listas.
Exercício 1: Faça programa que leia um vetor de 5 números inteiros e mostre-os."""

numeros = []
for n in range(1, 6):
    numero = int(input(f'Informe o {n}º valor: '))
    numeros.append(numero)
print(f'Os valores digitados foram: {numeros}.')

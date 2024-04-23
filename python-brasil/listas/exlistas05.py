"""Python Brasil
Lista de exercícios de listas.
Exercício 5: Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores."""

numeros = []
pares = []
impares = []
for n in range(1, 21):
    numero = int(input(f'Digite o {n}º número: '))
    numeros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os números digitados foram: {numeros}')
print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')

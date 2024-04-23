"""Python Brasil
Lista de exercícios de listas.
Exercício 9: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor."""

numeros = []
for n in range(1, 11):
    numero = int(input(f'Informe o {n}º número inteiro: '))
    numero = numero**2
    numeros.append(numero)
print(f'A soma dos quadrados dos elementos digitados é igual a: {sum(numeros)}.')

"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 7: Faça um programa que leia 5 números e informe o maior número."""

numeros = []
for c in range(1, 6):
    n = float(input('Digite um número: '))
    numeros.append(n)
print(f'O maior número informado foi: {max(numeros)}.')

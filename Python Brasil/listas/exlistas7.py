"""Python Brasil
Lista de exercícios de listas.
Exercício 7: Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números."""

numeros = []
multiplicacao = 1
for n in range(1, 6):
    numero = int(input(f'Digite o {n}º número: '))
    numeros.append(numero)
    multiplicacao *= numero
print(f'Os números digitados foram: {numeros}')
print(f'A soma dos números é igual a: {sum(numeros)}.')
print(f'A multiplicação dos números é igual a {multiplicacao}.')

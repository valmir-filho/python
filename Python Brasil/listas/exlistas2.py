"""Python Brasil
Lista de exercícios de listas.
Exercício 2: Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""

numeros = []
for n in range(1, 11):
    numero = float(input(f'Digite o {n}º número: '))
    numeros.append(numero)
numeros.reverse()
print(f'Os {len(numeros)} números digitados na ordem inversa são: {numeros}')

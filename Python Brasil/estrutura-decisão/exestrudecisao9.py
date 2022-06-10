"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 9: Faça um Programa que leia três números e mostre-os em ordem decrescente."""

print()
numeros = []
for i in range(3):
    num = float(input('\33[32mDigite um número: '))
    numeros.append(num)
print(sorted(numeros, reverse=True))

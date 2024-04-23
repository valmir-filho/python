"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 14: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a
quantidade de números impares."""

print()
par = impar = 0
for c in range(1, 11):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print()
print(f'Você digitou {par} números pares e {impar} números ímpares.')

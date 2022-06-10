"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 8: Faça um programa que leia 5 números e informe a soma e a média dos números."""

numeros = []
for c in range(1, 6):
    n = float(input('Digite um número: '))
    numeros.append(n)
print(f'A soma dos números informados é igual a: {sum(numeros)}.')
print(f'A média dos números informados é igual a: {sum(numeros)/c}')

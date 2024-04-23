"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 6: Faça um Programa que leia três números e mostre o maior deles."""

numeros = []
for i in range(3):
    num = float(input('Digite um número qualquer: '))
    numeros.append(num)
print('O maior número digitado é o: {}'.format(max(numeros)))

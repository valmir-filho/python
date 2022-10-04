"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 7: Faça um Programa que leia três números e mostre o maior e o menor deles."""

num1 = float(input('Digite o 1º número: '))
num2 = float(input('Digite o 2º número: '))
num3 = float(input('Digite o 3º número: '))
if (num1 == num2) and (num1 == num3):
    print('Os números são iguais')
else:
    if num1 > num2 and num1 > num3:
        print('O maior número é:', num1)
    elif num2 > num3:
        print('O maior número é:', num2)
    else:
        print('O maior número é:', num3)
    if num1 < num2 and num1 < num3:
        print('O menor número é:', num1)
    elif num2 < num3:
        print('O menor número eh:', num2)
    else:
        print('O menor número é:', num3)

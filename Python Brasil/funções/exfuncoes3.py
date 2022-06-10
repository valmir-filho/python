"""Python Brasil
Lista de exercícios de funcões.
Exercício 3: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""


def somar(a, b, c):
    s = a + b + c
    print(f'A soma dos 3 argumentos é igual a: {s}.')


somar(a=int(input('Digite o 1º valor: ')),
      b=int(input('Digite o 2º valor: ')),
      c=int(input('Digite o 3º valor: ')))

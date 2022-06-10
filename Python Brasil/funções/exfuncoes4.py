"""Python Brasil
Lista de exercícios de funcões.
Exercício 4: Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere "P",
se o seu argumento for positivo, e "N", se o seu argumento for zero ou negativo."""


def rertorna(a):
    if a > 0:
        print('Resultado: "P"')
    else:
        print('Resultado: "N"')


rertorna(int(input('Digite um número inteiro: ')))

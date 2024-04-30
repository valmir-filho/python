"""
Empacotamento e desempacotamento de argumentos em funções no Python.

O "*args" em Python é um recurso que permite que uma função aceite um número variável de argumentos posicionais (ou seja, argumentos não nomeados). O termo "args" é apenas uma convenção; você pode escolher qualquer nome que desejar, mas o uso do asterisco (*) antes do nome da variável é importante para indicar que você está trabalhando com argumentos posicionais variáveis.

O nome "args" é uma convenção, mas o uso do "*" é necessário para indicar que é uma lista de argumentos posicionais variáveis.

Você pode usar qualquer nome em vez de "args", mas a maioria das pessoas usa esse nome por convenção.

Os argumentos passados para a função com o "*args" são acessíveis como uma tupla dentro da função. Você pode iterar sobre essa tupla ou acessar elementos específicos por índice.

O "*args" permite criar funções flexíveis que podem lidar com diferentes números de argumentos posicionais, tornando-as úteis em situações em que você não sabe antecipadamente quantos argumentos serão passados.
"""


def minha_funcao(*args):
    for arg in args:
        print(arg)


# Chamando a função com diferentes números de argumentos
minha_funcao(1, 2, 3)
minha_funcao("a", "b")
minha_funcao(10, "x", True)

# def soma(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# resultado = soma(1, 2, 3, 4)
# print(f"O resultado é {resultado}.")

# def soma(*args):
#     total = sum(args)
#     return total


# resultado = soma(1, 2, 3, 4)
# print(f"O resultado é {resultado}.")

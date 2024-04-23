# Unidade 06: Funções
"""Diferentemente de outras linguagens de programação, o Python permite que seja retornado mais de um valor a partir de
uma função. Esse retorno pode ser capturado como uma tupla, sendo os valores acessados de forma individual a partir de
cada índice"""

# Exemplo de aplicação 4: Elabore um aplicativo que recorra a uma função que receba diversos valores numéricos e
# retorne o maior e o menor valor da lista.

def valores(*numeros):
    maior = -1000000
    menor = 1000000
    for numero in numeros:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    return maior, menor
resultado = valores(7,15,3,22,1,8)
print('O maior número é: {} e o menor número é: {}.'.format(resultado[0], resultado[1]))

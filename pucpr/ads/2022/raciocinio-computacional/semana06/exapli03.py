# Unidade 06: Funções
"""Exemplo de aplicação 3: Elabore um programa que use uma função chamada somar(), que efetue a soma de uma quantidade
aleatória de números informados, retornando o resultado da operação."""

def somar(*numeros):
    soma = 0
    for c in numeros:
        soma += c
    return soma
valores = somar(2,3,4,5,8)
print('A soma dos números é: {}.'.format(valores))

# Unidade 06: Funções
"""Exercício de fixação 3: Crie um programa que receba uma lista de números e retorne a média."""

def media(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)
resultado = media(2, 5, 9, 4, 11)
print(f'O valor da média é: {resultado}.')

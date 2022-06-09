# Unidade 06: Funções
"""Exercício de fixação 2: Crie um programa que calcule o fatorial de um número, mas de forma recursiva, ou seja,
chamando a função fatorial de dentro dela mesma."""

def fatorial(numero):
    if numero == 0:
        return 1
    return numero * fatorial(numero - 1)
numero = int(input('Digite um número inteiro para calcular seu fatorial: '))
fat = fatorial(numero)
print(f'O fatorial de {numero} é {fat}.')

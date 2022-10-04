# Unidade 04: Listas.
"""Exercício de aplicação 1: Elabore um programa que solicite ao usuário cinco números, armazene-os em uma lista e exiba como resultado os dados
 obtidos."""

lista_numeros = []
for i in range(5):
    numero = float(input('Informe um número: '))
    lista_numeros.append(numero)
print('Os números digitados são: {}'.format(lista_numeros))

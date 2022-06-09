# Unidade 06: Funções
"""Crie uma função que receba uma quantidade de números indeterminada e retorne:
— 3 valores e a soma de todos os elementos da lista;
— 1 lista com os números pares;
— 1 lista com os números ímpares."""

def separar_numeros(*numeros):
    soma = 0
    par = []
    impar = []
    for c in numeros:
        soma += c
        if c % 2 == 0:
            par.append(c)
        else:
            impar.append(c)
    return soma, par, impar
soma, par, impar = separar_numeros(1,2,3,4,5,6,7,8,9)
print(soma)
print(par)
print(impar)

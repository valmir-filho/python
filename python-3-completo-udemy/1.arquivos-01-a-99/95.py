"""
Função "itertools.zip_longest()".

A função "itertools.zip_longest()" é uma alternativa à função "zip()" que permite combinar vários iteráveis, mas ao contrário do "zip()", que para quando a sequência mais curta se esgota, o "zip_longest()" continua combinando elementos até que todos os iteráveis tenham sido completamente percorridos. Quando um dos iteráveis é esgotado, em vez de parar a combinação, ele preenche os valores ausentes com um valor de preenchimento especificado, que é fornecido como argumento "fillvalue".

"""

import itertools

numeros = [1, 2, 3, 4, 5]
letras = ["a", "b", "c"]

combinacao = itertools.zip_longest(numeros, letras, fillvalue="x")

for numeros, letras in combinacao:
    print(f"Combinação de número e letra: {numeros, letras}.")

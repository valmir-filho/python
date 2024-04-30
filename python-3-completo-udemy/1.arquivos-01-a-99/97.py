"""
Função "itertools.count(start, step)".

A função "itertools.count(start, step)" da biblioteca "itertools" no Python é usada para criar um iterador infinito que gera uma sequência de números inteiros a partir de um valor inicial (start) com um determinado passo (step). Ela é útil em situações em que você precisa de uma sequência numérica infinita ou quando deseja criar um contador personalizado.

Aqui está a sintaxe da função itertools.count():

- start: o valor a partir do qual a sequência deve começar. É opcional e, se não especificado, o valor padrão é zero.

- step: o valor pelo qual a sequência será incrementada a cada iteração. Também é opcional, e o valor padrão é 1 se não especificado.
"""

import itertools

contador = itertools.count(start=1, step=2)

for _ in range(5):
    print(next(contador))

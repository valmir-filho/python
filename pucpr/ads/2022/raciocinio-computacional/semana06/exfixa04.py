# Unidade 06: Funções
"""Exercício de fixação 4: documente a função fatorial() desenvolvida no exercício de fixação 1
desta unidade."""

def fatorial(numero: int):
    """
    Calcula o fatorial de um número

    :param numero: número base para o cálculo do fatorial.
    :return: resultado do cálculo do fatorial.
    """
    if numero == 0:
        return 1
    fat = 1
    for i in range(numero, 0, -1):
        fat *= i
    return fat

# Crie uma função que multiplique todos os argumentos não nomeados recebidos e retorne o total em uma variável, mostrando o seu valor.


def multiplicacao(*args):
    total = 1
    for arg in args:
        total *= arg
    return total


resultado = multiplicacao(5, 5, 5, 5, 5)
print(f"O resultado da multiplicação é {resultado}.")

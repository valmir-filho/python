# Exercício: crie uma função que calcular se o número é par ou ímpar.


def par_impar(numero):
    return f"O número {numero} é par." if numero % 2 == 0 else f"O número {numero} é ímpar."


resultado = par_impar(7)
print(resultado)


# def par_impar(numero):
#     if numero % 2 == 0:
#         return f"O número {numero} é par."
#     return f"O número {numero} é ímpar."


# resultado = par_impar(8)
# print(resultado)

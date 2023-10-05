"""
Higher-Order Functions.

As funções de ordem superior (Higher-Order Functions) são um conceito importante na programação funcional e estão disponíveis em Python. Basicamente, uma função de ordem superior é uma função que aceita outras funções como argumentos e/ou retorna funções como resultados. Isso significa que você pode tratar funções como cidadãos de primeira classe em Python, passando-as para outras funções e retornando-as de funções.
As funções de ordem superior tornam o código mais flexível e conciso, permitindo que você trabalhe com funções de maneira mais dinâmica e reutilizável. Elas são uma parte importante da programação funcional em Python.
"""


def processa_lista(lista, funcao):
    resultado = []
    for elemento in lista:
        resultado.append(funcao(elemento))
    return resultado


# Função que duplica um número
def duplica(numero):
    return numero * 2


# Função que soma 10 a um número
def soma_10(numero):
    return numero + 10


numeros = [1, 2, 3, 4, 5]

# Usando a função processa_lista com a função duplica
resultado_duplicado = processa_lista(numeros, duplica)
print(resultado_duplicado)

# Usando a função processa_lista com a função soma_10
resultado_adicionado = processa_lista(numeros, soma_10)
print(resultado_adicionado)

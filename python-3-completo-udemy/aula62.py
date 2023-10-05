# Exercício: crie funções que duplique, triplique e quadriplique um número recebido como parâmetro.

"""
Neste código, a função calculadora recebe uma função "operacao" como parâmetro e retorna uma função interna "executar" que aplica a operação ao número fornecido como argumento. Dessa forma, você pode criar instâncias separadas da função calculadora para as operações de duplicação, triplicação e quadriplicação e usá-las conforme necessário.
"""


def calculadora(operacao):
    def executar(numero):
        return operacao(numero)
    return executar


def duplicar(numero):
    return numero * 2


def triplicar(numero):
    return numero * 3


def quadriplicar(numero):
    return numero * 4


resultado_duplicar = calculadora(duplicar)
resultado_triplicar = calculadora(triplicar)
resultado_quadriplicar = calculadora(quadriplicar)

numero = 2

print(f"O número {numero} duplicado é {resultado_duplicar(numero)}.")
print(f"O número {numero} triplicado é {resultado_triplicar(numero)}.")
print(f"O número {numero} quadriplicado é {resultado_quadriplicar(numero)}.")


"""
Este código cria uma função chamada "criar_multiplicacao" que retorna uma função interna "multiplicar". A função interna "multiplicar" aceita um número como argumento e retorna uma string que descreve o resultado de multiplicar esse número pelo "multiplicador" que foi passado como argumento para a função externa "criar_multiplicacao".
"""


# def criar_multiplicacao(multiplicador):
#     def multiplicar(numero):
#         return f" O número {numero} multiplicado por {multiplicador} é {numero * multiplicador}."
#     return multiplicar


# resultado_duplicar_numero = criar_multiplicacao(2)
# resultado_triplicar_numero = criar_multiplicacao(3)
# resultado_quadruplicar_numero = criar_multiplicacao(4)

# print(resultado_duplicar_numero(2))
# print(resultado_triplicar_numero(2))
# print(resultado_quadruplicar_numero(2))

"""
Escopo de função no Python.

Em Python, o escopo (ou âmbito) refere-se à visibilidade e acessibilidade de variáveis em diferentes partes de um programa.
O escopo é fundamental para entender como as variáveis funcionam em funções e em outros blocos de código. 

1) Escopo local

    - As variáveis definidas dentro de uma função são chamadas de variáveis locais.
    - Elas são acessíveis apenas dentro da própria função onde foram declaradas.
    - Variáveis locais são criadas quando a função é chamada e destruídas quando a função retorna ou conclui sua execução.

2) Escopo global

    - As variáveis definidas fora de qualquer função são chamadas de variáveis globais.
    - Elas são acessíveis de qualquer lugar do programa, incluindo dentro de funções.
    - Variáveis globais permanecem em escopo durante toda a execução do programa.

3) Escopo local e global

    - Se uma variável local tiver o mesmo nome que uma variável global, a variável local terá precedência dentro da função.
    - No entanto, se você precisar modificar uma variável global de dentro de uma função, você deve usar a palavra-chave "global".

4) Escopo encadeado (nested scope)

    - É possível definir funções dentro de funções (funções aninhadas).
    - As funções internas têm acesso ao escopo da função externa, mas as funções externas não têm acesso ao escopo das funções internas.

Em resumo, o escopo em Python define onde uma variável é acessível e influencia a visibilidade de variáveis em funções.
Entender o escopo é fundamental para escrever código Python eficiente e sem erros. Certifique-se de atribuir variáveis globais quando necessário e de evitar confusões entre variáveis locais e globais com nomes semelhantes.
"""

# Exemplo (escopo local)


def funcao1():
    x = 10  # x é uma variável local
    print(f"Valor de x: {x}.")


# funcao1()  # Chamando a função
# # x não é acessível aqui fora
# # print(x)  # Gerará um erro, pois "x" não está definido de maneira global


# # Exemplo (escopo global)
# y = 20  # y é uma variável global


# def funcao2():
#     # Podemos acessar a variável global y dentro da função
#     print(f"Valor de y: {y}.")


# funcao2()  # Chamando a função
# # não gerará um erro, pois "y" está definido de maneira global
# print(f"Valor de y: {y}.")

# # Exemplo (escopo local e global)
# z = 30  # z é uma variável global


# def alterar_z():
#     global z  # Informando que queremos acessar a variável global z
#     z = 40  # Modificando a variável global z


# alterar_z()
# print(f"Valor de z: {z}.")  # Agora z foi alterada para 40


# # Exemplo (escopo encadeado ou nested scope)


# def externa():
#     a = 50

#     def interna():
#         b = 60
#         # A função interna tem acesso à variável "a" da função externa
#         print(f"Valor de a + b: {a + b}.")

#     interna()


# externa()

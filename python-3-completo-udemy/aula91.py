"""
Variáveis livres e nonlocal no Python.

No Python, as "variáveis livres" e a função "nonlocal" estão relacionadas ao escopo das variáveis em funções aninhadas (funções definidas dentro de outras funções).

Vamos entender cada um desses conceitos:

- Variáveis livres (free variables): as "variáveis livres" são variáveis que estão definidas em um escopo superior ao da função interna (função aninhada) e são referenciadas dentro dessa função. Essas variáveis são "livres" no sentido de que não são locais à função interna nem globais; elas pertencem ao escopo da função que envolve a função interna. No entanto, a função interna pode acessá-las e usá-las.

- A palavra-chave "nonlocal" é usada em uma função interna para indicar que uma variável que está definida em um escopo superior ao da função interna (um escopo não global) deve ser tratada como uma variável daquele escopo superior, em vez de criar uma nova variável local com o mesmo nome. Isso é útil quando você deseja modificar o valor de uma variável em um escopo superior a partir de uma função interna.

Em resumo, "variáveis livres" são aquelas que são definidas em escopos superiores e referenciadas em funções internas, enquanto "nonlocal" é usado para modificar variáveis de escopos superiores a partir de funções internas. Esses conceitos são úteis para entender o comportamento das variáveis em funções aninhadas no Python.
"""

# Exemplo variáveis livres


def funcao_externa():
    x = 10

    def funcao_interna():
        print(x)  # "x" é uma variável livre

    funcao_interna()


funcao_externa()

"""
Neste exemplo, a variável "x" é uma variável livre dentro da "funcao_interna", pois ela é definida na "funcao_externa" e é referenciada dentro da "funcao_interna".
"""

# Exemplo nonlocal


# def funcao_externa():
#     x = 10

#     def funcao_interna():
#         nonlocal x  # "x" não é mais uma variável livre
#         x = 20
#         print(x)

#     funcao_interna()
#     print(x)


# funcao_externa()

"""
Neste exemplo, a palavra-chave "nonlocal" é usada na "funcao_interna" para indicar que a variável "x" não é uma variável local, mas sim a variável "x" da "funçao_externa". Portanto, quando você altera o valor de "x" na "funcao_interna", essa alteração é refletida também na "funçao_externa".
"""

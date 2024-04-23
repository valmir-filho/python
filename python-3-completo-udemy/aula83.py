"""
Generation function.

Principais conceitos e características da generetion function no Python:

- Para criar uma função geradora, você usa a palavra-chave yield em vez de return. Quando a função é chamada, ela retorna um objeto de gerador, mas a execução da função é suspensa em vez de encerrada.

- Suspensão e retomada: quando você chama uma função geradora, ela não executa o código imediatamente. Em vez disso, ela retorna um objeto de gerador, que permite a suspensão e a retomada da execução da função a partir do ponto onde ela foi suspensa.

- Iteração sob demanda: os elementos gerados por um gerador são produzidos sob demanda à medida que você os itera. Isso significa que apenas um elemento é calculado e retornado de cada vez, economizando memória e recursos.

- Lazy evaluation: a técnica de lazy evaluation é usada nos geradores. Isso significa que os valores não são calculados até que sejam solicitados, o que é particularmente útil quando você está trabalhando com sequências de tamanho desconhecido ou muito grandes.
"""


def gerador_simples():
    yield 1
    yield 2
    yield 3


# Criação de um objeto de gerador
objeto_gerador = gerador_simples()

print(next(objeto_gerador))
# print(next(objeto_gerador))
# print(next(objeto_gerador))
# print(next(objeto_gerador))

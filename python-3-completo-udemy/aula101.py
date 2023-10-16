"""
Função "partial()" no Python.

No Python, o módulo "functools" fornece a função "partial", que permite criar funções parcialmente aplicadas. Uma função parcialmente aplicada é uma função que "trava" alguns dos argumentos de uma função maior e retorna uma nova função que pode ser chamada com os argumentos restantes. Isso pode ser útil em situações em que você deseja criar funções especializadas a partir de funções mais genéricas, evitando a duplicação de código.

A assinatura da função "functools.partial" é a seguinte:

functools.partial(func, *args, **keywords)

- func: é a função que você deseja parcialmente aplicar.

- *args: são os argumentos posicionais a serem fixados (travados) na função.

- **keywords: são os argumentos de palavra-chave (argumentos nomeados) a serem fixados na função.

O uso de "functools.partial" é útil quando você deseja criar funções especializadas a partir de funções mais genéricas, economizando tempo e evitando repetição de código. Isso também torna o código mais legível e mais modular, uma vez que você pode criar funções específicas sem repetir toda a lógica da função original.
"""

from functools import partial

# Função que multiplica dois números


def multiplicar(a, b):
    return a * b


# Função parcialmente aplicada que sempre multiplica por 2
dobrar = partial(multiplicar, 2)

resultado = dobrar(5)  # Isso é equivalente a chamar multiplicar(2, 5)

print(resultado)

"""
Neste exemplo, a função "multiplicar" aceita dois argumentos e retorna o produto desses argumentos. Usamos "functools.partial" para criar uma função chamada "dobrar" que é uma versão parcialmente aplicada de "multiplicar". Fixamos o primeiro argumento em 2, de modo que quando chamamos "dobrar(5)", é equivalente a chamar "multiplicar(2, 5)".
"""

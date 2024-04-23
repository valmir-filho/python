"""
Função "filter()" no Python.

A função "filter" no Python é uma função embutida que permite filtrar elementos de um iterável (como uma lista, tupla, ou conjunto) com base em uma função de teste. Ela cria um novo iterável contendo apenas os elementos do iterável original para os quais a função de teste retorna "True". A assinatura da função `filter` é a seguinte:

filter(função, iterável)

- função: é a função de teste que será aplicada a cada elemento do iterável. A função de teste deve retornar "True" ou "False".

- iterável: é o iterável do qual você deseja filtrar os elementos.

A função "filter" é útil quando você deseja criar uma nova coleção que contenha apenas os elementos que atendem a um determinado critério ou condição. Isso é especialmente útil quando você deseja filtrar dados com base em alguma lógica específica em vez de processar todos os elementos do iterável original.
"""


def e_par(numero):
    return numero % 2 == 0


números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtra apenas os números pares
números_pares = list(filter(e_par, números))

print(números_pares)

"""
Neste exemplo, a função "e_par" é usada como a função de teste. A função "filter" aplica a função "e_par" a cada número na lista "números" e retorna um iterável contendo apenas os números pares. O resultado é uma lista de números pares, que é então impressa no console.
"""

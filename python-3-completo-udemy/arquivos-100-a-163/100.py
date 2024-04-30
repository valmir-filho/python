"""
Função "map()" no Python.

A função "map" no Python é uma função incorporada que permite aplicar uma função a cada item de um iterável (por exemplo, uma lista) e retorna um novo iterável com os resultados dessas aplicações. A assinatura da função "map" é a seguinte:

map(função, iterável, ...)

- função: é a função que você deseja aplicar a cada elemento do iterável. Pode ser uma função definida pelo usuário ou uma função embutida no Python.

- iterável: é a sequência de elementos aos quais você deseja aplicar a função. Pode ser uma lista, tupla, conjunto, ou outro iterável.

A função "map" retorna um objeto de mapa (um iterador), que você pode converter em uma lista ou outro tipo de iterável, se necessário.

A função "map" é útil quando você deseja aplicar uma função a todos os elementos de uma coleção e obter uma nova coleção com os resultados das operações. Isso pode ser útil para transformar os dados de uma lista, realizar cálculos em cada elemento, ou aplicar qualquer função que atue em itens individuais de um iterável.
"""


def dobrar_numero(numero):
    return numero * 2


numeros = [1, 2, 3, 4, 5]
resultado = map(dobrar_numero, numeros)

# Converte o objeto map em uma lista
lista_resultado = list(resultado)

print(lista_resultado)

"""
Neste exemplo, a função "dobrar_numero" dobra o valor de um número passado como argumento. A função "map" aplica essa função a cada elemento da lista "numeros", resultando em um iterador de map. Em seguida, o iterador de map é convertido em uma lista usando "list(resultado)", e a lista final contém os resultados das chamadas da função "dobrar_numero" para cada elemento da lista original.
"""

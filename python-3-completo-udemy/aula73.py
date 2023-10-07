"""
List comprehension no Python.

A list comprehension (compreensão de lista) no Python é uma construção sintática que permite criar listas de maneira concisa e elegante, aplicando uma expressão a cada item de uma sequência (como uma lista, tupla, string ou range) e, opcionalmente, filtrando os itens com base em uma condição. List comprehensions são uma maneira poderosa e eficiente de criar listas em Python.

A sintaxe geral de uma list comprehension é a seguinte:

[nova_lista_expression for item in sequencia if condicao]

Aqui está o significado de cada parte:

- nova_lista_expression: é a expressão que será aplicada a cada item da sequência, e o resultado será adicionado à nova lista.

- item: é a variável temporária que representa cada elemento da sequência.

- sequencia: é a sequência (lista, tupla, string, range, etc.) da qual você está criando a nova lista.

- condicao (opcional): é uma condição que você pode adicionar para filtrar os itens da sequência. Apenas os itens que atendem a essa condição serão incluídos na nova lista.
"""

# Exemplo de criação de uma lista usando o comando for
lista_for = []
for numero in range(10):
    lista_for.append(numero)
print(lista_for)

# Exemplo de criação de uma lista usando o list comprehension
lista_comprehension = [numero for numero in range(10)]
print(lista_comprehension)

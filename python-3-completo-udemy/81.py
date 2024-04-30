"""
Iteráveis e Iteradores no Python.

Em Python, iteráveis e iteradores são conceitos importantes relacionados à iteração (percorrer elementos) de sequências de dados, como listas, tuplas, dicionários e strings. Eles são fundamentais para a criação de loops e para a manipulação de dados em coleções.

1) Iterável (iterable): um objeto iterável é qualquer objeto capaz de ser percorrido elemento por elemento. Em Python, os iteráveis são aqueles que podem ser usados em um loop for e também são frequentemente passados para funções que aceitam sequências de elementos, como sum, list, tuple, etc. Exemplos comuns de iteráveis em Python incluem listas, tuplas, strings, conjuntos e dicionários.

2) Iterador (iterator): um iterador é um objeto que permite a iteração sobre os elementos de um iterável. O iterador mantém um estado interno que rastreia a posição atual na sequência. Ele fornece dois métodos principais: __iter__() (que retorna o próprio iterador) e __next__() (que retorna o próximo elemento na sequência).

Observação: é importante notar que, após atingir o final de um iterável, um iterador levanta a exceção "StopIteration" se você tentar acessar o próximo elemento. Portanto, é uma boa prática usar loops for ou lidar com exceções ao usar explicitamente next(). O loop "for" no Python é uma maneira conveniente de usar iteradores sem a necessidade de criar um iterador explicitamente. Quando você usa um loop for para percorrer um iterável, ele cria um iterador interno automaticamente.
"""

# Exemplo iterável
objeto = [1, 2, 3, 4, 5]
# objeto = 42

if hasattr(objeto, "__iter__"):
    print(f"O objeto {objeto} é iterável.")
else:
    print(f"O objeto {objeto} não é iterável.")

# Exemplo iterador
# lista = [1, 2, 3, 4, 5]
# meu_iterador = iter(lista)
# meu_iterador = lista.__iter__()
# tupla = 1, 2, 3, 4, 5

# print(lista.__iter__())
# print(next(meu_iterador))
# print(tupla.__iter__())

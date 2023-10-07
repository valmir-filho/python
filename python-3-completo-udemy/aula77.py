"""
Dictionary comprehension (compreensão de dicionário) no Python.

É uma construção sintática que permite criar dicionários de maneira concisa, aplicando uma expressão a cada par de chave-valor em uma sequência (como uma lista, tupla ou outra estrutura iterável). A sintaxe geral de uma Dictionary Comprehension é a seguinte:

{chave: valor for elemento in sequencia}

Aqui está o significado de cada parte:

- chave: é a expressão que determina a chave em cada par chave-valor no dicionário resultante.
- valor: é a expressão que determina o valor em cada par chave-valor no dicionário resultante.
- elemento: é a variável temporária que representa cada elemento na sequência.
- sequencia: é a sequência (lista, tupla, outra estrutura iterável, etc.) da qual você está criando o dicionário.

Você também pode usar funções personalizadas nas expressões para criar dicionários mais complexos ou aplicar lógica personalizada a cada elemento da sequência.

Dictionary comprehension é uma ferramenta poderosa e eficaz para criar dicionários em Python de maneira concisa e legível. É especialmente útil quando você deseja transformar ou processar dados de uma sequência em um dicionário de uma maneira rápida e eficiente.
"""

# Exemplo: criando um dicionário de quadrados de números em uma lista
numeros = [1, 2, 3, 4, 5]
quadrados = {x: x**2 for x in numeros}
print(quadrados)

# Exemplo: convertendo uma lista de palavras em um dicionário com os seus tamanhos
palavras = ["python", "é", "incrível"]
tamanhos = {word: len(word) for word in palavras}
print(tamanhos)

# Exemplo: filtrando pares chave-valor em um dicionário com base em uma condição
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
pares_filtrados = {chave: valor for chave,
                   valor in dicionario.items() if valor % 2 == 0}
print(pares_filtrados)

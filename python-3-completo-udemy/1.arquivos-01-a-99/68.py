"""
Empacotamento e desempacotamento de dicionários no Python.

Se referem à técnica de manipular dicionários de forma eficiente, seja para passar argumentos em funções ou para criar e atualizar dicionários. Isso é feito usando o operador **.

O empacotamento de dicionários ocorre quando você coleta vários argumentos de palavras-chave em um único dicionário. Isso é útil quando você deseja passar um conjunto de argumentos de palavras-chave para uma função.

O desempacotamento de dicionários ocorre quando você extrai pares de chave-valor de um dicionário e os usa como argumentos de palavras-chave em uma função ou para criar um novo dicionário.
"""

# Empacotamento de dicionários
"""
Neste exemplo, o dicionário dados é empacotado e os valores são desempacotados na chamada da função criar_pessoa usando **dados. Isso cria um novo dicionário com os mesmos pares de chave-valor.
"""


def criar_pessoa(nome, idade, cidade):
    pessoa = {'nome': nome, 'idade': idade, 'cidade': cidade}
    return pessoa


dados = {'nome': 'Alice', 'idade': 30, 'cidade': 'Nova York'}
pessoa = criar_pessoa(**dados)
print(pessoa)

# Desempacotamento de dicionários
"""
No primeiro exemplo, os valores do dicionário dados são desempacotados como argumentos da função saudacao. No segundo exemplo, dois dicionários são combinados em um novo dicionário usando o desempacotamento.

O empacotamento e o desempacotamento de dicionários são úteis quando você lida com funções que aceitam muitos argumentos de palavras-chave ou quando deseja combinar ou atualizar dicionários de maneira eficiente. Isso torna seu código mais limpo e legível.
"""


def saudacao(nome, idade):
    print(f"Olá, {nome}! Você tem {idade} anos.")


dados = {'nome': 'Alice', 'idade': 30}
# Saída: Olá, Alice! Você tem 30 anos.
saudacao(**dados)

# Criando um novo dicionário
dados1 = {'nome': 'Alice', 'idade': 30}
dados2 = {'cidade': 'Nova York'}
novo_dicionario = {**dados1, **dados2}
# Saída: {'nome': 'Alice', 'idade': 30, 'cidade': 'Nova York'}
print(novo_dicionario)

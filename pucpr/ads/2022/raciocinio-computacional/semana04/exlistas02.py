# Unidade 04: Listas.
""""Funções built in são funções internas da linguagem que podem ser utilizadas sobre determinado objeto. No caso do
Python, existem algumas funções que podem ser aplicadas sobre listas, facilitando a execução de alguns algoritmos que
teriam de ser desenvolvidos pelo programador para realizar as mesmas funções."""

# Função len() retornando a quantidade de elementos de uma lista.
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(nums))

# Função len() retornando a quantidade de caracteres de uma ‘string’.
nome = 'Python'
print(len(nome))

# Função max() retornando o maior valor dentro de uma lista de números.
lista = [9, 3, 6, 14, 5, 2]
print(max(lista))

# Função max() retornando o maior valor dentro de uma lista com ‘strings’. Nesse caso, a função toma como base a ordem
# alfabética.
herois = ['Zorro', 'Hulk', 'Spiderman', 'Batman']
print(max(herois))

# Função min() retornando o menor valor dentro de uma lista de números.
lista = [9, 3, 6, 14, 5, 2]
print(min(lista))

# Função min() retornando o menor valor dentro de uma lista com ‘strings’. Nesse caso, a função toma como base a ordem
# alfabética.
herois = ['Zorro', 'Hulk', 'Spiderman', 'Batman']
print(min(herois))

# Função sorted() retornando a lista de números em ordem crescente.
lista = [9, 3, 6, 14, 5, 2]
print(sorted(lista))

# Função sorted() retornando a lista de ‘strings’ em ordem alfabética (de A-Z).
herois = ['Zorro', 'Hulk', 'Spiderman', 'Batman']
print(sorted(herois))

# Função sorted() retornando a lista de números em ordem decrescente. Nesse caso, utilizamos o parâmetro "reverse".
lista = [9, 3, 6, 14, 5, 2]
print(sorted(lista, reverse=True))

# Função sorted() retornando a lista de ‘strings’ em ordem alfabética (de Z-A).
herois = ['Zorro', 'Hulk', 'Spiderman', 'Batman']
print(sorted(herois, reverse=True))

# Função sum() retornando a soma de todos os elementos de uma lista.
lista = [9, 3, 6, 14, 5, 2]
print(sum(lista))

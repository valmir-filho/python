# Aplicações de variáveis compostas em Python.
# Listas (são mutáveis a qualquer momento).

n = [2, 5, 9, 1, 4, 2, 2]
print(n)
n[3] = 11  # Alterei a posição 3 da lista.
print(n)
n.append(7)  # Adicionei um elemento (7) na lista.
print(n)
n.sort()  # Ordenei a lista em ordem crescente.
print(n)
n.sort(reverse=True)  # Ordenei a lista em ordem decrescente.
print(n)
print(len(n))  # Imprime quantos elementos tem a lista.
n.insert(3, 6)  # Adicionou o número 6 na posição 3.
print(n)
n.pop()  #  O comando "pop" sem parâmetro, elimina sempre o último elemento da lista.
print(n)
n.pop(2)  # Elimina o elemento da posição 2 da lista.
print(n)
n.remove(2)  # Remove o elemento 2 da lista (sempre o 1º encontrado, da esquerda para a direita).
print(n)
if 5 in n:  # Procura o número 5 na lista.
    n.remove(5)  # Remove o número 5 na lista.
print(n)

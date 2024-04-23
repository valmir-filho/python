# Unidade 04: Listas.
""""Comandos para trabalhar com listas no Python."""

lista1 = [17, 33, 8, 11, 8, 15, 9]
lista2 = [3, 7]
print(lista1)
print(lista2)

# Inclui o elemento 10 no final da lista 1.
lista1.append(10)
print(lista1)

# Inclui a lista 2 dentro da lista 1.
lista1.extend(lista2)
print(lista1)

# Insere um número escolhido dentro de uma posição definida da lista (nesse caso, está a inserir o número 0 na posição
# 2 da Lista 1).
lista1.insert(2, 0)
print(lista1)

# Remove um elemento escolhido de uma lista (nesse caso, eliminará o número 11 da Lista 1).
lista1.remove(11)
print(lista1)

# Remove e retorna um elemento escolhido de uma lista (nesse caso, o elemento da posição 7 da Lista 1).
print(lista1.pop(7))
print(lista1)

# Cria uma cópia de uma determinada lista (nesse caso, cria uma cópia da Lista 1).
copia_lista1 = lista1.copy()
print(copia_lista1)

# Remove todos os elementos de uma lista (nesse caso, elimina todos os elementos da Lista 1).
lista1.clear()
print(lista1)

# Conta quantos elementos (escolhido) existem em uma determinada lista (nesse caso, quantos elementos iguais a 8 existem
# na Lista 1).
lista1 = copia_lista1.copy()
print(lista1.count(8))

# Ordena a lista em ordem crescente (nesse caso, ordena a Lista 1).
lista1.sort()
print(lista1)

# Inverte os elementos de uma lista (nesse caso, a Lista 1).
lista1.reverse()
print(lista1)

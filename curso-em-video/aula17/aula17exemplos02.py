# Aplicações de variáveis compostas em Python.
# Listas (são mutáveis a qualquer momento).

numeros_1 = list()
numeros_1.append(2)
numeros_1.append(4)
numeros_1.append(6)
for n in numeros_1:
    print(n)  # Imprime todos os números da lista um embaixo do outro.
for n in numeros_1:
    print(n, end= ' ')  # Imprime todos os números da lista um ao lado do outro.
print()
for c, n in enumerate(numeros_1):  # Comando enumerate pega tanto a chave, quanto o valor dela.
    print(f'Na posição {c} encontrei o valor {n}.')

numeros_2 = list()
for cont in range(1, 6):
    numeros_2.append(int(input('Digite um valor: ')))  # Incluiu os valores digitados pelo usuário em uma lista vazia.
print(numeros_2)

a = [2, 3, 4, 7]
b = a
b[2] = 9  # Importante: apesar de alterar apenas a posição 2 da lista b, o Python altera também na lista a, pois ele cria uma ligação entre as duas listas.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:]  # Nesse caso, foi criada uma cópia da lista a em b.
b[2] = 9  # Como a lista é apenas uma cópia, nesse caso, altera-se somente o elemento da posição 2 na lista b.
print(f'Lista A: {a}')
print(f'Lista B: {b}')

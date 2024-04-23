# Aplicações de variáveis compostas em Python.
# Listas em listas.

teste = list()  # Criei uma lista chamada teste.
teste.append('Valmir')  # Inclui 'Valmir' na lista teste.
teste.append(40)  # Inclui '40' na lista teste.
print(teste)
galera = list()  # Criei uma lista chamada galera.
galera.append(teste[:])  # Inclui a lista teste na lista galera.
print(galera)
teste[0] = 'Pedro'
teste[1] = 25
galera.append(teste[:])
print(galera)
galera_2 = [['João', 33], ['Pedro', 12], ['Ana', 70], ['Lucas', 23]]  # Outra forma de criar listas em listas.
print(galera_2)
print(galera_2[0])  # Imprime todas as informações da posição '0' da lista.
print(galera_2[0][0])  # Imprime apenas a informação da posição '0' da lista que está na lista.
for p in galera_2:
    print(p)  # Imprime as informações da lista.
for p in galera_2:
    print(p[0])  # Imprime apenas os nomes da lista.

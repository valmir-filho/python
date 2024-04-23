# Unidade 06: Funções
# Funções no Python
# Ela pode ser usada diversas vezes no mesmo script, alterando apenas os seus dados.

# Definindo uma função com 1 parâmetro apenas.
def minha_funcao(nome):
    print('Good morning,', nome)
minha_funcao('John')
minha_funcao('Peter')
print()
# Definindo uma função com mais de 1 parâmetro.
def minha_funcao1(nome, dia):
    if dia:
        print('Good morning', nome)
    else:
        print('Good night', nome)
minha_funcao1('John', True)
minha_funcao1('John', False)
print()
# Função recebendo vários numeros.
def somar(*numeros):
    soma = 0
    for c in numeros:
        soma += c
    print(soma)
somar(1, 3, 5, 7, 9)
print()
def somar(*numeros):
    soma = 0
    for c in numeros:
        soma += c
    return soma
valor = somar(1, 3, 5, 7, 9)
print(valor)
print()
# Aplicação de uma função.
def filtar_numeros(lista):
    nova_lista = []
    cont = 0
    for c in lista:
        if c % 2 ==0:
            nova_lista.append(c)
        else:
            cont += 1
    return cont, nova_lista
removidos, lista = filtar_numeros([1, 2, 3, 4, 5, 6])
print(removidos)
print(lista)

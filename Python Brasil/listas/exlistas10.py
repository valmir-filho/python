"""Python Brasil
Lista de exercícios de listas.
Exercício 10: Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores."""

lista_num_1 = []
lista_num_2 = []
lista_num_3 = []
for n in range(1, 11):
    num_1 = int(input(f'Digite o {n} número da lista 1: '))
    lista_num_1.append(num_1)
    lista_num_3.append(num_1)
    num_2 = int(input(f'Digite o {n} número da lista 2: '))
    lista_num_2.append(num_2)
    lista_num_3.append(num_2)
print(f'A lista 1 digitada foi: {lista_num_1}')
print(f'A lista 2 digitada foi: {lista_num_2}')
print(f'A lista 3 (intercalação entre as listas 1 e 2) é: {lista_num_3}')

# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exemplo de aplicação 2: Elabore um programa que crie uma tupla contendo duas listas com dados, altere os dados da
primeira lista e verifique se ocorre mudança de dados da tupla."""

tupla_com_lista = ([1, 2, 3], [4, 5, 6])
print(id(tupla_com_lista[0]))
tupla_com_lista[0].append(9)
print(tupla_com_lista)
print(id(tupla_com_lista[0]))

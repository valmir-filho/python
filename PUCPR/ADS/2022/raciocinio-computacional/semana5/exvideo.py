# Unidade 05: Estrutura de dados: tuplas e dicionários
print()
# Criação de um dicionário.
frutas = {'cod1': 'Laranja', 'cod2': 'Maçã', 'cod3': 'Banana', 'cod4': 'Morango', 'cod5': 'Manga'}
print(frutas)
print()
# Adicionando mais um item no dicionário.
frutas['cod6'] = 'Abacate'
print(frutas)
print()
# Alterando um item no dicionário.
frutas['cod6'] = 'Morango'
print(frutas)
print()
# Excluindo um item do dicionário.
del frutas['cod6']
print(frutas)
print()
# Listando todos os itens do dicionário.
for i in frutas.values():
    print(i)
print()
# Listando todas as chaves do dicionário.
for i in frutas.keys():
    print(i)
print()
# Listando todos os itens do dicionário, com as suas respectivas chaves.
retorno = frutas.items()
print(retorno)
print()
# Listando todos os itens do dicionário, com as suas respectivas chaves, usando a estrutura de repetição for.
for key, item in frutas.items():
    print(key, item)
print()
# Incluindo uma lista dentro de um dicionário.
# frutas = {'cod1': 'Laranja', 'cod2': 'Maçã', 'cod3': 'Banana', 'cod4': 'Morango', 'cod5': 'Manga'}. Apenas para conferir o dicionário.
frutas['cod6'] = ['Alface', 'Tomate', 'Couve']
for key, item in frutas.items():
    print(key, item)

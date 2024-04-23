# Aplicações de variáveis compostas em Python.
# Dicionários

pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': 22}
print(pessoas)  # Imprime o dicionário inteiro.
print(pessoas['Sexo'])  # Imprime a informação da chave sexo.
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')  # No print formatado, o que vai nos colchetes tem que estar entre aspas duplas.
print(pessoas.keys())  # Imprime as chaves do dicionário.
print(pessoas.values())  # Imprime os valores do dicionário.
print(pessoas.items())  # Imprime o dicionário inteiro.
for k in pessoas.keys():  # Imprime as chaves do dicionário.
    print(k)
for v in pessoas.values():  # Imprime os valores do dicionário.
    print(v)
for k, v in pessoas.items():  # Imprime os itens do dicionário.
    print(f'{k} = {v}')
del pessoas['Nome']  # Apaga as informações referente a chave nome.
print(pessoas)
pessoas['Sexo'] = 'F'  # Altera o valor do sexo dentro do dicionário.
print(pessoas)
pessoas['Peso'] = 75  # Adicionei a chave "Peso" e o valor "75" no dicionário.
print(pessoas)

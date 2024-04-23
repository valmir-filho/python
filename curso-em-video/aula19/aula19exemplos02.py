# Aplicações de variáveis compostas em Python.
# Dicionários

estado1 = {'UF': 'Paraná', 'Sigla': 'PR'}
estado2 = {'UF': 'Santa Catarina', 'Sigla': 'SC'}
brasil = [estado1, estado2]  # Incluí os 2 dicionários na lista.
print(brasil)
print(brasil[0])  # Imprime o dicionário da posição "0" da lista.
print(brasil[0]['UF'])  # Imprime o valor da chave "UF" da posição "0" da lista.

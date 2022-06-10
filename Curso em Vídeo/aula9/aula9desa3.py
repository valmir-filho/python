# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# A função strip serve para eliminar os espaços (antes ou depois da digitação).
# A função upper serve troca tudo para maiúsculo.
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[0:5].upper() == 'SANTO')

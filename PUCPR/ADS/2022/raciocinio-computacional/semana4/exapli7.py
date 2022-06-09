# Unidade 04: Listas.
"""Exemplo de aplicação 7: solicite ao usuário que entre com diversos nomes, informando de forma separada nome e último
sobrenome. Ao final, mostre uma lista de nomes no formato: sobrenome, nome. Para encerrar a entrada de dados, basta o
usuário inserir no nome o texto “sair”."""

import time

nomes = []
print()
print('Instruções: Você deve informar o nome e o último sobrenome. Para finalizar, digite "SAIR" no "nome".')
print()
while True:
    nome = str(input('Digite o nome: ')).strip().upper()
    if nome == 'SAIR':
        break
    sobrenome = str(input('Digite o sobrenome: ')).strip().upper()
    nome_completo = [nome, sobrenome]
    nomes.append(nome_completo)
print()
print('Gerando as listas...')
time.sleep(3)
print()
for nome in nomes:
    print(nome[1] + ', ' + nome[0])

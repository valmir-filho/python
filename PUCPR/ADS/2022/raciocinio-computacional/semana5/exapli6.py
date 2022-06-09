# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exemplo de aplicação 6: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda,
exibindo, ao final, o dicionário."""

agenda = {}
print('*** Cadastro de telefones ***')
while True:
    contato = str(input('Digite o nome do contato: ')).strip()
    telefone = str(input('Digite o telefone do contato: ')).strip()
    agenda[contato] = telefone
    if str(input('Deseja cadastrar um novo contato (S=sim/N=não): ').strip().upper()) == "N":
        break
print(agenda)

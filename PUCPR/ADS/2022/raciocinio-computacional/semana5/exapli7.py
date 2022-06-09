# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exemplo de aplicação 7: Elabore um programa que simule o cadastro de telefones com dicionário como uma agenda.
Caso seja informado um nome já existente, deve perguntar se deseja alterar os dados existentes. Caso seja um telefone
já existente, deve informar que esse telefone já está cadastrado em outro contato, não podendo ser efetuada a inclusão.
Ao final, deve exibir o dicionário."""

agenda = {}
print('*** Cadastro de telefones ***')
while True:
    contato = str(input('Digite o nome do contato: ')).strip()
    telefone = str(input('Digite o telefone do contato: ')).strip()
    if contato in agenda:
        if str(input('Contato já cadastrado com o número {}. Deseja alterar? (S=sim/N=não) '.format(agenda[contato]))).strip().upper() == "N":
            continue
    if telefone in agenda.values():
        print('Telefone já cadastrado em outro contato.')
        continue
    agenda[contato] = telefone
    if str(input('Deseja cadastrar um novo contato (S=sim/N=não): ').strip().upper()) == "N":
        break
print(agenda)

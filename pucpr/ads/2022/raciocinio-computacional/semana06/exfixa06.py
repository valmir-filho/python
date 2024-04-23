# Unidade 06: Funções
"""Exercício de fixação 6: Crie um programa que, fazendo uso de funções, cadastre contatos em uma agenda telefônica,
podendo excluí-los. Deve ser exibido um menu com as opções: inserir, remover e sair."""

def receber_dados_contato():
    nome = str(input('Digite o nome do contato: ')).strip().upper()
    telefone = input('Digite o telefone do contato: ')
    return nome, telefone
def inserir(agenda):
    contato = receber_dados_contato()
    if contato[0] in agenda:
        if str(input('Contato já cadastrado. Deseja alterar o telefone? (S=sim/N=não) ')).strip().upper() == 'N':
            return False
    agenda[contato[0]] = contato[1]
    return True
def remover(nome, agenda):
    if nome in agenda:
        del agenda[nome]
        return True
    else:
        return False
def menu():
    print('*** Agenda Telefônica ***')
    print('[1] - Inserir contato')
    print('[2] - Remover contato')
    print('[3] - Sair')
    return int(input('Escolha uma das opções: '))
agenda = {}
while True:
    op = menu()
    if op == 1:
        if inserir(agenda):
            print('Contato cadastrado com sucesso')
            print(agenda)
        else:
            print('Operação não realizada')
    elif op == 2:
        nome = input('Digite o nome do contato a ser removido: ')
        if remover(nome, agenda):
            print('Contato removido com sucesso')
            print(agenda)
        else:
            print('Operação não realizada')
    else:
        print('Até a próxima!')
        break

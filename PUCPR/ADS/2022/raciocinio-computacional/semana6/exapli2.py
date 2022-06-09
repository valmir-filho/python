# Unidade 06: Funções
"""Exemplo de aplicação 2: Elabore um programa que cadastre contatos de uma agenda telefônica. A função de cadastro deve
ser realizada dentro de uma função chamada inserir, que recebe como parâmetros o nome e o telefone do contato, bem como
a agenda de contatos. A função deve verificar se o contato já existe e, em caso positivo, perguntar se o telefone deve
ser modificado, retornando true ou false, de acordo com a inclusão/modificação executada ou não na agenda."""

agenda_telefonica = {}
def inserir(nome, telefone, agenda):
    if nome in agenda:
        contato = str(input('Contato já cadastrado. Deseja alterar o telefone? (S=sim/N=não) ')).strip().upper()
        if contato == 'N':
            return False
    agenda[nome] = telefone
    return True
while True:
    nome = str(input('Digite o nome do contato: ')).strip().upper()
    telefone = int(input('Digite o telefone do contato: '))
    if inserir(nome, telefone, agenda_telefonica):
        print('Contato adicionado ou atualizado com sucesso!')
    else:
        print('Falha ao tentar adicionar o contato!')
    novo_contato = str(input('Gostaria de adicionar um novo contato? (S=sim/N=não) ')).strip().upper()
    if novo_contato == 'N':
        break
print(agenda_telefonica)

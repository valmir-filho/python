# Unidade 06: Funções
"""Exemplo de aplicação 1: Elabore um programa que cadastre contatos de uma agenda telefônica. A função de cadastro deve
ser realizada dentro de uma função chamada inserir, que recebe como parâmetros o nome e o telefone do contato, bem como
a agenda de contatos."""

agenda_telefonica = {}
def inserir(nome, telefone, agenda):
    agenda[nome] = telefone
while True:
    nome = str(input('Digite o nome do contato: ')).strip().upper()
    telefone = int(input('Digite o telefone do contato: '))
    inserir(nome, telefone, agenda_telefonica)
    novo_contato = str(input('Gostaria de adicionar um novo contato? (S=sim/N=não) ')).strip().upper()
    if novo_contato == "N":
        break
print(agenda_telefonica)

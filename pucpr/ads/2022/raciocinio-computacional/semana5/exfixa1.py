# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exercício de fixação 1: Crie um programa que efetue o cadastro de pessoas com nome, RG e CPF por meio de tuplas,
adicionando-as a uma lista e imprimindo essa lista no fim do programa."""

cadastro = []
while True:
    nome = str(input('Digite o seu nome: ')).strip().upper()
    rg = int(input('Digite apenas os números do seu RG: '))
    cpf = int(input('Digite apenas os números do seu CPF: '))
    pessoa = (nome, rg, cpf)
    cadastro.append(pessoa)
    if str(input('Gostaria de cadastrar mais uma pessoa? (S=sim/N=não) ')).strip().upper() == 'N':
        break
print(cadastro)

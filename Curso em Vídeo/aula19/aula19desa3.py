"""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
se por acaso a CTPS diferir de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar."""

import datetime
dados = {'nome': str(input('Digite o seu nome: ')).strip().upper(),
         'idade': int(input('Digite o seu ano de nascimento: ')),
         'ctps': int(input('Digite a sua CTPS: '))}
dados['idade'] = datetime.date.today().year - dados['idade']
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Digite o seu ano de contratação: '))
    dados['salario'] = float(input('Digite o seu salário: R$'))
    dados['aposentadoria'] = ((35 - (datetime.date.today().year - dados['contratacao'])) + dados['idade'])
    for k, v in dados.items():
        print(f'{k} tem o valor {v}.')
else:
    for k, v in dados.items():
        print(f'{k} tem o valor {v}.')

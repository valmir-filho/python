# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exemplo de aplicação 5: Elabore um programa que recorra a uma tupla chamada Endereco, contendo dados nomeados."""

from collections import namedtuple
endereco = namedtuple('endereco', ['logradouro', 'numero', 'bairro', 'cidade', 'estado'])
endereco_puc = endereco(logradouro = 'Rua Imaculada Conceição', numero = 1555, bairro = 'Prado Velho', cidade = 'Curitiba', estado = 'PR')
print('Endereço: {}'.format(endereco_puc.logradouro))
print('Número: {}'.format(endereco_puc.numero))
print('Bairro: {}'.format(endereco_puc.bairro))
print('Cidade: {}'.format(endereco_puc.cidade))
print('Estado: {}'.format(endereco_puc.estado))

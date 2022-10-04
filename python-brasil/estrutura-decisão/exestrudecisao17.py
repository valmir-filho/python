"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 17: Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano
é ou não bissexto."""

from datetime import date
print()
print('=' * 43)
print('Programa para verificar se o ano é bissexto')
print('=' * 43)
print()
ano = int(input('Digite um ano qualquer. Se quiser verificar o ano atual, digite "0": '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('A ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

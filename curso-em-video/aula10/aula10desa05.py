# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Digite um ano qualquer. Se quiser analisar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('A ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))

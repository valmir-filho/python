"""Faça um programa que leia o ano de nascimento de um jovem e informe, conforme a sua idade:
— Se ele ainda vai se alistar ao serviço militar;
— Se é a hora de se alistar;
— Se já passou o tempo de alistamento.
O programa também precisa mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
ano_nasc = int(input('Informe o seu ano de nascimento: '))
sexo = str(input('Informe o seu sexo (F=feminino/M=masculino): ')).strip().upper()
if sexo == 'M':
    if (date.today().year - ano_nasc) < 18:
        print('Você ainda vai se alistar. Falta(m) {} ano(s).'.format(18 - (date.today().year - ano_nasc)))
    elif (date.today().year - ano_nasc) == 18:
        print('Está na hora de você se alistar.')
    else:
        print('Já passou o tempo de alistamento em {} ano(s).'.format((date.today().year - ano_nasc) - 18))
else:
    print('Você não precisa servir as forças armadas.')

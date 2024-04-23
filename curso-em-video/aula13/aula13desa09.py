""""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores."""

from datetime import date
maior21 = 0
menor21 = 0
for pessoa in range(1, 8):
    ano_nasc = int(input('Informe o ano de nascimento da pessoa {}: '.format(pessoa)))
    if (date.today().year - ano_nasc) > 21:
        maior21 += 1
    else:
        menor21 += 1
print('{} pessoas já atingiram a maior idade e {} pessoas ainda não atingiram.'.format(maior21, menor21))

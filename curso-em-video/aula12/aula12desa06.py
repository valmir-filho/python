"""A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua
categoria, de acordo com a idade:
— Até 9 anos: mirim;
— De 10 a 14 anos: infantil;
— De 15 a 19 anos: junior;
— 20 anos: sênior;
— Acima de 20 anos: master."""

from datetime import date
ano_nasc = int(input('Informe o seu ano de nascimento: '))
if (date.today().year - ano_nasc) <= 9:
    print('A sua categoria é: MIRIM')
elif 10 < (date.today().year - ano_nasc) <= 14:
    print('A sua categoria é: INFANTIL')
elif 15 < (date.today().year - ano_nasc) <= 19:
    print('A sua categoria é: JUNIOR')
elif (date.today().year - ano_nasc) == 20:
    print('A sua categoria é: SÊNIOR')
else:
    print('A sua categoria é: MASTER')


# Python Brasil
# Lista de exercícios de estrutura sequencial.
# Exercício 13: Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas: para homens: (72.7*h)-58 e para mulheres: (62.1*h)-44.7.

sexo = str(input('Informe o seu sexo (M/F): ')).strip().upper()
altura = float(input('Informe a sua altura (em metros): '))
if sexo == 'M':
    print('O seu peso ideal é: {:.2f}'.format(72.7 * altura - 58))
else:
    print('O seu peso ideal é: {:.2f}'.format(62.1 * altura - 44.7))

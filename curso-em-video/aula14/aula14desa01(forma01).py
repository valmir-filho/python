"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
digitação novamente até ter um valor correto."""

while True:
    sexo = str(input('Informe o sexo da pessoa: ')).strip().upper()
    if sexo == 'M' or sexo == 'F':
        print('Sexo {} informado com sucesso!'.format(sexo))
        break
    else:
        print('Valor inválido! Digite novamente.')

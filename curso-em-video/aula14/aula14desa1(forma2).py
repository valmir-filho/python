"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
digitação novamente até ter um valor correto."""

sexo = str(input('Informe o sexo da pessoa: ')).strip().upper()[0]  # Esse "[0]" serve para pegar a 1ª letra da string digitada, se houver (foi utilizado o fatiamento).
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Informe o sexo da pessoa: ')).strip().upper()[0]
print('Sexo {} informado com sucesso!'.format(sexo))

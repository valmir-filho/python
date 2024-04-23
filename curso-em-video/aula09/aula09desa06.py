# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.
# Exemplo:
# Nome: Ana Maria de Souza
# Primeiro nome: Ana
# Último nome: Souza

nome_completo = str(input('Digite o seu nome completo: ')).strip()
print('Muito prazer {}!!!'.format(nome_completo))
nome = nome_completo.split()
print('O seu 1º nome é: {}'.format(nome[0]))
print('O seu último nome é: {}'.format(nome[len(nome)-1]))

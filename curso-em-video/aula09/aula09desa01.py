# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas;
# * O nome com todas minúsculas;
# * Quantas letras (sem considerar os espaços);
# * Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
# Função strip serve para eliminar os espaços vazios (se existirem) antes e depois do(s) nome(s).
print('Analisando seu nome...')
print('Seu nome em maiúsculas fica: {}'.format(nome.upper()))
print('Seu nome em minúsculas fica: {}'.format(nome.lower()))
print('O seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
# O "find" vai procurar no mome, o que estiver entre as aspas.
separa = nome.split()
print('O seu primeiro nome é: {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
# Outra forma de apresentar quantas letras tem o primeiro nome.

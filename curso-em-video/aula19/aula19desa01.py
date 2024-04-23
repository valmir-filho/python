"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
conteúdo da estrutura na tela."""

aluno = {'Nome': str(input('Digite o nome do aluno: ')).strip().upper(),
         'Media': float(input('Digite a média do aluno: '))}
print(f'Nome é igual a {aluno["Nome"]}.')
print(f'Média é igual a {aluno["Media"]}')
if aluno["Media"] >= 7:
    print(f'Situação igual a Aprovado!')
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno["Media"] < 7:
    print(f'Situação igual a Recuperação!')
    aluno['situacao'] = 'Recuperação'
else:
    print(f'Situação igual a Reprovado!')
    aluno['situacao'] = 'Reprovado'

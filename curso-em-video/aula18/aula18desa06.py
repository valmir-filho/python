"""Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre
um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""

alunos = list()
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().upper()
    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    continuar = str(input('Deseja cadastrar mais um aluno? (S=sim/N=Não): ')).strip().upper()
    if continuar == 'N':
        break
print('…' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('…' * 30)
while True:
    opc = int(input('Deseja mostrar notas de qual aluno? (Digite 999 para interromper): '))
    if opc == 999:
        print('Encerrando...')
        break
    if opc <= len(alunos) - 1:
        print(f'As notas do aluno {alunos[opc][0]} são: {alunos[opc][1]}')
print('Obrigado por utilizar o programa!')

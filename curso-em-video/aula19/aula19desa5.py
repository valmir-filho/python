"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) A média de idade do grupo;
c) Uma lista com todas as mulheres;
d) Uma lista com todas as pessoas com idade acima da média."""

dados = {}
pessoas = []
soma = media = 0
while True:
    dados['nome'] = str(input('Digite o nome da pessoa: ')).strip().upper()
    while True:
        dados['sexo'] = str(input('Digite o sexo da pessoa (M=masc/F=fem): ')).strip().upper()
        if dados['sexo'] == 'M' or dados['sexo'] == 'F':
            break
        print('Valor inválido! Digite apenas "M" ou "F".')
    dados['idade'] = int(input('Digite a idade da pessoa: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    while True:
        continuar = str(input('Deseja cadastrar mais uma pessoa? (S=sim/N=não): ')).strip().upper()
        if continuar == 'S' or continuar == 'N':
            break
        print('Valor inválido! Digite apenas "S" ou "N".')
    if continuar == 'N':
        break
print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
media = soma / len(pessoas)
print(f'A média de idade do grupo é de {media:.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print()
print('As pessoas com idade acima da média são: ', end='')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]}', end=' ')

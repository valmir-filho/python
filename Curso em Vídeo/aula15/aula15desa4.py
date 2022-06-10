""""Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos;
b) Quantos homens foram cadastrados;
c) Quantas mulheres tem menos de 20 anos."""

maiores_18 = homens = mulheres_menos_20 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo (M=masc./F=fem.): ')).strip().upper()[0]
    if idade > 18:
        maiores_18 += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres_menos_20 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar cadastrando pessoas (S=sim/N=não)? ')).strip().upper()
    if continuar == 'N':
        break
print(f'{maiores_18} pessoas tem mais de 18 anos.')
print(f'Foram cadastrados {homens} homnes.')
print(f'{mulheres_menos_20} mulheres tem menos de 20 anos.')

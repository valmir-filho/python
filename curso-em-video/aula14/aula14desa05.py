"""Faça um programa que leia o 1º termo e a razão de um PA, mostrando os 10 primeiros termos."""

primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    contador += 1
print('Fim')

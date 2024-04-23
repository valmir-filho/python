"""Faça um programa que leia o 1º termo e a razão de um PA, mostrando os 10 primeiros termos. Após, pergunte ao
usuário se ele quer mais termos e mostre-os. Para encerrar, o usuário precisa informar o "0"."""

primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))
termo = primeiro_termo
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} → '.format(termo), end='')
        termo += razao
        contador += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('PA finalizada com {} termos mostrados.'.format(total))

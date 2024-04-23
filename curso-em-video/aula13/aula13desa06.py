""""Desenvolva um programa que leia o primeiro termo e a razão da uma PA. No final, mostre os 10 primeiros termos dessa
progressão."""

primeiro_termo = int(input('Informe o 1º termo da PA: '))
razao = int(input('Informe a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
print('Os 10 primeiros termos da PA de razão {} é igual a: '.format(razao), end='')
for c in range(primeiro_termo, decimo_termo + razao, razao):
    print('{}'.format(c), end= ' - ')
print('Fim!')

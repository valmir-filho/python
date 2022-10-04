"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 28: Faça um programa que calcule o valor total investido por um colecionador na sua coleção de CDs e o valor
médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um."""

total_cds = 0
media = []
while total_cds <= 0:
    quant_cds = int(input('Digite a quantidade de CDs disponíveis na sua coleção: '))
    if quant_cds <= 0:
        print('Quantidade inválida! Digite uma quantidade maior que 0.')
    else:
        break
for c in range(1, quant_cds+1):
    valor = 0
    while valor <= 0:
        valor = float(input(f'Informe o valor pago pelo CD {c} R$'))
        if valor <= 0:
            print('Valor inválido! Digite um valor maior que 0.')
        else:
            media.append(valor)
print(f'Você investiu R${sum(media):.2f} na sua coleção de CDs.')
print(f'O valor médio de cada CD é igual a R${sum(media)/quant_cds:.2f}.')

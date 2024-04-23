"""Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor mensal, sabendo que ela não vai
poder ceder 30% do salário, ou então o empréstimo será negado."""

print()
valor_bem = float(input('Informe o valor do bem a ser financiado (em R$): '))
salario = float(input('Informe o valor do seu salário (em R$): '))
duracao_anos = float(input('Informe a duração do empréstimo (em anos): '))
duracao_meses = duracao_anos * 12
if (valor_bem/duracao_meses) > (salario*0.7):
    print('Empréstimo negado! Ultrapassa 30% do seu salário!')
else:
    print('O valor mensal a ser pago pelo financiamento é de: R${:.2f}'.format(valor_bem/duracao_meses))

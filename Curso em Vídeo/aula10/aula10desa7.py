# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1.250,00, calcule um aumento de 10%. Para os iguais ou inferiores, o aumento é de 15%.

salario = float(input('Informe o valor do seu salário R$'))
if salario <= 1250:
    print('O valor do seu aumento será de R${:.2f}'.format(salario * 0.15))
else:
    print('O valor do seu aumento será de R${:.2f}'.format(salario * 0.10))

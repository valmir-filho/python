# Faça um algoritmo que leia o salário de um funcionárioe mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o valor do seu salário: R$'))
aumento = salario * 0.15
novo_salario = salario + aumento
print('O seu novo salário, com um aumento de 15% é: R${:.2f}'.format(novo_salario))

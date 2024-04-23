# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

valor_inic_prod = float(input('Informe o valor do produto: R$'))
desconto = valor_inic_prod * 0.05
valor_fin_prod = valor_inic_prod - desconto
print('O valor do produto com 5% de desconto é: R${:.2f}'.format(valor_fin_prod))

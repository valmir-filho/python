# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode
# comprar. Considere: US$1,00 = R$3,27.

din_cart = float(input('Informe quanto de dinheiro você tem na carteira: R$'))
cotacao_dolar = float(input('Informe a cotação do dólar hoje: US$'))
conversao = din_cart / cotacao_dolar
print('*' * 27)
print('Você pode comprar US${:.2f}'.format(conversao))
print('*' * 27)

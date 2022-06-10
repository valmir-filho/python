"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 27: Uma frutaria está vendendo frutas com a seguinte tabela de preços:
         Até 5 kg          Acima de 5 kg
Morango: R$2,50 por kg     R$2,20 por kg
Maçã:    R$1,80 por kg     R$1,50 por kg
Se o cliente comprar mais de 8 kg em frutas ou o valor total da compra ultrapassar R$25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em kg) de morangos e a quantidade (em kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente."""

print()
morango = float(input('Informe a quantidade de morangos (em kg): '))
maca = float(input('Informe a quantidade de maças (em kg): '))
if morango <= 5:
    valor_morango = morango * 2.5
else:
    valor_morango = morango * 2.2
if maca <= 5:
    valor_maca = maca * 1.8
else:
    valor_maca = maca * 1.5
fruta_total = morango + maca
valor_total = valor_morango + valor_maca
if fruta_total >= 8 or valor_total > 25:
    print('O valor total a ser pago é de: R${:.2f}'.format(valor_total * 0.9))
else:
    print('O valor total a ser pago é de: R${:.2f}'.format(valor_total))

""""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
pagamento:
— À vista dinheiro/cheque: 10% de desconto;
— À vista no cartão: 5% de desconto;
— Em até 2 vezes no cartão: preço normal;
— 3 vezes ou mais no cartão: 20% de juros."""

print()
valor_produto = float(input('Informe o valor do produto: R$'))
print()
print('*' * 70)
print('''FORMAS DE PAGAMENTO
Digite 1 para pagamento à vista com dinheiro/cheque: 10% de desconto.
Digite 2 para pagamento à vista com cartão: 5% de desconto.
Digite 3 para pagamento em até 2 vezes no cartão: preço normal.
Digite 4 para pagamento em até 3 vezes ou mais no cartão: 20% de juros.''')
print('*' * 70)
print()
forma_pagamento = int(input('Escolha a forma de pagamento: '))
if forma_pagamento == 1:
    print('Você ganhou 10% de desconto. O valor do produto fica: R${:.2f}.'.format(valor_produto * 0.9))
elif forma_pagamento == 2:
    print('Você ganhou 5% de desconto. O valor do produto fica: R${:.2f}.'.format(valor_produto * 0.95))
elif forma_pagamento == 3:
    prestacao = valor_produto / 2
    print('Você pagará 2 parcelas de R${:.2f}.'.format(prestacao))
elif forma_pagamento == 4:
    num_parcelas = int(input('Você quer pagar em quantas parcelas (3 ou mais)? '))
    total_pago = valor_produto * 1.2
    prestacao = total_pago / num_parcelas
    print('Você está pagando 20% de juros. O valor do produto fica {} parcelas de: R${:.2f}.'.
          format(num_parcelas, prestacao))
else:
    print('Opção inválida! Tente novamente.')

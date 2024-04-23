"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 26: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro.
Gasolina: até 20 litros, desconto de 4% por litro. Acima de 20 litros, desconto de 6% por litro. Escreva um algoritmo
que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$2,50 e o preço do
litro do álcool é R$ 1,90."""

print()
print('\33[34m$' * 45)
print('PROMOÇÃO!')
print('*Álcool*')
print('Até 20 litros: desconto de 3% por litro.')
print('Acima de 20 litros: desconto de 5% por litro.')
print('*Gasolina*')
print('Até 20 litros: desconto de 4% por litro.')
print('Acima de 20 litros: desconto de 6% por litro.')
print('$' * 45, '\33[m')
print()
tipo_comb = str(input('Informe o tipo de combustível (A-álcool / G-Gasolina): ')).strip().upper()
num_litros = float(input('Informe a quantidade de combustível (em litros): '))
if tipo_comb == 'A':
    if num_litros <= 20:
        print('Você ganhou um desconto de 3% por litro. O valor total a ser pago é de: R${:.2f}'.format(num_litros * (1.9 - 1.9 * 0.03)))
    else:
        print('Você ganhou um desconto de 5% por litro. O valor total a ser pago é de: R${:.2f}'.format(num_litros * (1.9 - 1.9 * 0.05)))
else:
    if num_litros <= 20:
        print('Você ganhou um desconto de 4% por litro. O valor total a ser pago é de: R${:.2f}'.format(num_litros * (2.5 - 2.5 * 0.04)))
    else:
        print('Você ganhou um desconto de 6% por litro. O valor total a ser pago é de: R${:.2f}'.format(num_litros * (2.5 - 2.5 * 0.06)))

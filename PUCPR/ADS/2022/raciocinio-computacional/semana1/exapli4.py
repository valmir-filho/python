# Unidade 01: Introdução à programação Python
# Exemplo de aplicação 4: solicite ao usuário dois produtos, com suas respectivas quantidades e preços,
# e mostre esses dados formatados como tabelas.

prod1 = input("Digite o nome do produto 1: ")
quant1 = int(input("Digite a quantidade do produto 1: "))
valor1 = float(input("Digite o valor do produto 1: "))
prod2 = input("Digite o nome do produto 2: ")
quant2 = int(input("Digite a quantidade do produto 2: "))
valor2 = float(input("Digite o valor do produto 2: "))
print(f'{"Produto":20}|{"Quantidade":^12}|{"Valor":>10}')
print(f'{prod1:20}|{quant1:^12}|{valor1:10.2f}')
print(f'{prod2:20}|{quant2:^12}|{valor2:10.2f}')

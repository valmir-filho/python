# Unidade 03: Estruturas de repetição.
# Exercício de fixação 9: Crie um programa que simule um carrinho de compras, solicitando o nome do produto (não pode ser vazio),
# o seu valor (valor decimal, positivo) e quantidade a ser comprada (valor inteiro, positivo). Ao incluir um produto,
# deve perguntar se o usuário deseja fechar o pedido ou incluir mais produtos. Todos os dados devem ser validados.
# Ao final da compra, deve ser informado o valor total do pedido.

print("Sistema de compras")
total = 0
continuar = True
while continuar:
    while True:
        produto = input('Informe o nome do produto a ser comprado: ')
        if produto != "":
            break
        else:
            print('Nome do produto inválido!')
    while True:
        try:
            valor = float(input('Informe o valor unitário do produto: '))
            if valor <= 0:
                print('O valor do produto deve ser maior que 0.')
            else:
                break
        except ValueError:
            print('Valor do produto inválido.')
    while True:
        try:
            quant = int(input('Informe a quantidade do produto a ser comprada: '))
            if valor <= 0:
                print('O valor do produto deve ser maior que 0.')
            else:
                break
        except ValueError:
            print('Valor do produto inválido.')

    total += quant * valor

    resp = input('Produto inserido com sucesso. Deseja comprar mais algum produto (s/n)? ')
    if resp == "n":
        continuar = False
print(f'Valor total da compra: R$ {total:.2f}')

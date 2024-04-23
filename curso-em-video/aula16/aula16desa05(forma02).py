"""Crie um programa que tenha uma tupla única com nomes de produtos e os seus respectivos preços na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = ('Calça', 123.52, 'Camisa', 114.32, 'Camiseta', 80.62, 'Tênis', 221.52, 'Blusa', 240.42)
print('≈' * 39)
print(f'{"LISTA DE PREÇOS":^40}')
print('≈' * 39)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('≈' * 39)

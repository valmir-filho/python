"""Crie um programa que tenha uma tupla única com nomes de produtos e os seus respectivos preços na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular."""

produtos = ('Calça', 123.52, 'Camisa', 114.32, 'Camiseta', 80.62, 'Tênis', 221.52, 'Blusa', 240.42)
print('-' * 41)
print(f'{"RELAÇÃO DE PRODUTOS":^41}')
print('-' * 41)
print('{}{:.>29}{:>7}'.format(produtos[0], 'R$', produtos[1]))
print('{}{:.>28}{:>7}'.format(produtos[2], 'R$', produtos[3]))
print('{}{:.>26}{:>7}'.format(produtos[4], 'R$', produtos[5]))
print('{}{:.>29}{:>7}'.format(produtos[6], 'R$', produtos[7]))
print('{}{:.>29}{:>7}'.format(produtos[8], 'R$', produtos[9]))
print('-' * 41)

"""Python Brasil
Lista de exercícios de estrutura sequencial.
Exercício 16: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total."""

import time
altura = float(input('\33[32mInforme a altura da região a ser pintada (em  metros): '))
largura = float(input('Informe a largura da região a ser pintada (em metros): \33[m'))
area = altura * largura
print()
print('Calculando a área a ser pintada...')
time.sleep(3)
print('A área a ser pintada tem: {:.2f} metros quadrados\33[m'.format(area))
print()
print('Calculando a quantidade de tinta gasta...')
time.sleep(3)
quant_tinta_gasta = area / 3
print('A quantidade de tinta gasta é de: {:.2f} litros'.format(quant_tinta_gasta))
print()
quant_lata = quant_tinta_gasta / 18
print('Você precisará de {:.2f} latas de tinta'.format(quant_lata))
custo = quant_lata * 80
print('Você gastará R${:.2f}'.format(custo))

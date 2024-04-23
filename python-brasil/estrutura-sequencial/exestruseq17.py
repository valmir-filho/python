"""Python Brasil
Lista de exercícios de estrutura sequencial.
Exercício 17: Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$80,00 ou em galões de 3,6 litros, que custam R$25,00."""

from time import sleep
altura = float(input('\33[32m Informe a altura da área a ser pintada (em metros): '))
largura = float(input('Informe a largura da área a ser pintada (em metros): \33[m'))
area = altura * largura
print()
print('Calculando a área a ser pintada...')
time.sleep(3)
print('A área a ser pintada é de {:.2f} metros quadrados.'.format(area))
tinta_gasta = area / 6
print()
print('Calculando a quantidade de tinta gasta...')
time.sleep(3)
print('A quantidade de tinta gasta é de: {:.2f} litros.'.format(tinta_gasta))
print()
total_gasto_lata = tinta_gasta / 18
total_gasto_galao = tinta_gasta / 3.6
print('Calculando o total gasto...')
time.sleep(3)
print('\33[31mVocê gastará R${:.2f} se comprar a tinta em lata e R${:.2f} se comprar a tinta em galão.\33[m'.format(total_gasto_lata * 80, total_gasto_galao * 25))

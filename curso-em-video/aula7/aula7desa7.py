# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Informe o valor da largura da parede (em m): '))
altura = float(input('Informe o valor da altura da parede (em m): '))
area = largura * altura
gasto_tinta = area / 2
print('A parede de {:.2f}x{:.2f} tem área igual a: {:.2f} m2'.format(largura, altura, area))
print('Você precisará de {:.1f} litros de tinta para pintar essa parede.'.format(gasto_tinta))

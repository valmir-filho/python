# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
angulo = float(input('Informe um ângulo qualquer: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {}º, possui:\nSeno igual a: {:.2f} radianos\nCosseno igual a: {:.2f} radianos\n'
      'Tangente igual a: {:.2f} radianos'.format(angulo, seno, cosseno, tangente))

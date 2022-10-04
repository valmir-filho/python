# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

from math import hypot
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot(cat_oposto, cat_adjacente)
print('O valor da hipotenusa é: {:.2f}'.format(hipotenusa))

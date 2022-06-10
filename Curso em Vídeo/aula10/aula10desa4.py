# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por
# km para viagens de até 200 km e R$0,45 para viagens mais longas.

import time
from time import sleep
distancia = int(input('Qual é a distância da viagem? (em km): '))
print('Processando...')
time.sleep(3)
if distancia <= 200:
    print('O valor da sua passagem será de: R${:.2f}'.format(distancia * 0.5))
else:
    print('O valor da sua passagem será de: R${:.2f}'.format(distancia * 0.45))

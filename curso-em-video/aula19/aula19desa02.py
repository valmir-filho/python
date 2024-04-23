"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado."""

from random import randint
import time
count = 1
valores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
           'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('Valores sorteados:')
for k, v in valores.items():
    print(f'O {k} tirou: {v} no dado.')
    time.sleep(1)
print('Ranking dos jogadores:')
for c in sorted(valores, key=valores.get, reverse=True):
    print(f'{count}º lugar: ', end='')
    count += 1
    print(f'{c} com o valor {valores[c]}.')
    time.sleep(1)

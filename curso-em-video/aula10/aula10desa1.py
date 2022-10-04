# Escreva um programa que faça o computador "pensar" num número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

from random import randint
from time import sleep
computador = randint(0, 5)
num_digitado = int(input('Tente advinhar um número entre 0 e 5 que eu estou pensando, digite ele: '))
print('Processando...')
sleep(2)
if num_digitado == computador:
    print('Você venceu!!!')
else:
    print('Você perdeu!!!')

"""Faça um programa onde o computador vai "pensar" em um número entre 0 e 10. Porém, o jogador vai tentar advinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer."""

import random
palpites = 0
while True:
    numero_pensado_computador = random.randint(0,10)
    numero_digitado_usuario = int(input('Tente advinhar o número entre 0 e 10 que eu estou pensando: '))
    if numero_pensado_computador == numero_digitado_usuario:
        print('Você acertou! Eu pensei no número {} e você digitou o número {}.'.format(numero_pensado_computador, numero_digitado_usuario))
        palpites += 1
        break
    else:
        print('Você errou! Eu pensei no número {} e você digitou o número {}.'.format(numero_pensado_computador, numero_digitado_usuario))
        palpites += 1
print('Você precisou de {} palpites para acertar.'.format(palpites))

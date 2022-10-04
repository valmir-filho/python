"""Faça um programa onde o computador vai "pensar" em um número entre 0 e 10. Porém, o jogador vai tentar advinhar
até acertar, mostrando no final quantos palpites foram necessários para vencer."""

import random
palpites = 0
while True:
    numero_pensado_computador = random.randint(0,10)
    print('Tente advinhar o número entre 0 e 10 que eu estou pensando...')
    numero_digitado_usuario = int(input('Digite o seu palpite: '))
    if numero_pensado_computador == numero_digitado_usuario:
        print('Você acertou! Eu pensei no número {} e você digitou o número {}.'.format(numero_pensado_computador, numero_digitado_usuario))
        palpites += 1
        break
    else:
        if numero_pensado_computador > numero_digitado_usuario:
            print('Você errou! Vou dar uma dica...O número que eu pensei é maior do que o que você digitou.')
            palpites += 1
        else:
            print('Você errou! Vou dar uma dica...O número que eu pensei é menor do que o que você digitou.')
            palpites += 1
print('Você precisou de {} palpites para acertar.'.format(palpites))

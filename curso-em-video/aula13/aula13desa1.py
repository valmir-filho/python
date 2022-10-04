""""Faça um programa que mostre uma contagem regressiva na tela para estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles."""

import time
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('Feliz Ano Novo! 🎇🎇🎇')

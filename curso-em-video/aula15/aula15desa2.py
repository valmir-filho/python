"""Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada número digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo."""

import time

print('∞' * 27)
print('PROGRAMA GERADOR DE TABUADA')
print('∞' * 27)

while True:
    print()
    n = int(input('Informe um número qualquer para gerar a sua tabuada.\nPara sair, digite um número negativo: '))
    if n < 0:
        print()
        print('Obrigado por utilizar o programa 👏👏👏!')
        break
    else:
        print()
        print(f'Gerando a tabuada do {n}...')
        time.sleep(2)
        for c in range(0, 11):
            print(f'{n} x {c} = {n * c}')

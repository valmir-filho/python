"""Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import sample
from time import sleep
print('♾️' * 25)
print('PROGRAMA GERADOR DE JOGOS DA MEGA-SENA')
print('♾️' * 25)
jogos = []
jogo = int(input('Informe quantos jogos deseja fazer: '))
print('♾️' * 25)
print('Gerando os jogos...')
sleep(2)
for j in range(1, jogo + 1):
    numeros = sample(range(1, 61), 6)
    jogos.append(sorted(numeros))
    print(f'Jogo {j}:', jogos[0])
    sleep(2)
    jogos.clear()
print('♾️' * 25)
print(f'{"BOA SORTE!":>25}')

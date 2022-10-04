""""Crie um programa que faça o computador jogar Jokenpô com você."""

import time
import random
print()
print('=-=' * 4)
print('JOGO JOKENPÔ')
print('=-=' * 4)
print()
itens = ('Papel', 'Pedra', 'Tesoura')
pontuacao_computador = 0
pontuacao_usuario = 0
while True:
    escolha_computador = random.randint(0, 2)
    escolha_usuario = int(input('Escolha do usuário ([0]-Papel / [1]-Pedra / [2]-Tesoura): '))
    print()
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PÔ')
    print()
    print('*' * 30)
    print('Escolha do computador: {}.'.format(itens[escolha_computador]))
    print('Escolha do usuário: {}.'.format(itens[escolha_usuario]))
    print('*' * 30)
    print()
    if escolha_computador == 0:
        if escolha_usuario == 0:
            print('Essa rodada empatou.')
        elif escolha_usuario == 1:
            print('O computador ganhou.')
            pontuacao_computador = pontuacao_computador + 1
        elif escolha_usuario == 2:
            print('O usuário ganhou.')
            pontuacao_usuario = pontuacao_usuario + 1
        else:
            print('Jogada inválida! Tente novamente.')
    if escolha_computador == 1:
        if escolha_usuario == 0:
            print('O usuário ganhou.')
            pontuacao_usuario = pontuacao_usuario + 1
        elif escolha_usuario == 1:
            print('Essa rodada empatou.')
        elif escolha_usuario == 2:
            print('O computador ganhou.')
            pontuacao_computador = pontuacao_computador + 1
        else:
            print('Jogada inválida! Tente novamente.')
    if escolha_computador == 2:
        if escolha_usuario == 0:
            print('O computador ganhou.')
            pontuacao_computador = pontuacao_computador + 1
        elif escolha_usuario == 1:
            print('O usuário ganhou.')
            pontuacao_usuario = pontuacao_usuario + 1
        elif escolha_usuario == 2:
            print('Essa rodada empatou.')
        else:
            print('Jogada inválida! Tente novamente.')
    print()
    print('*' * 29)
    print('Pontuação do computador: {}.'.format(pontuacao_computador))
    print('Pontuação do usuário: {}.'.format(pontuacao_usuario))
    print('*' * 29)
    print()
    jogar_novamente = str(input('Deseja jogar novamente? (S=sim/N=não): ')).strip().upper()
    print()
    if jogar_novamente == 'S':
        continue
    else:
        if pontuacao_computador > pontuacao_usuario:
            print('Computador venceu com {} ponto(s).'.format(pontuacao_computador))
        elif pontuacao_computador < pontuacao_usuario:
            print('Usuário venceu com {} ponto(s). '.format(pontuacao_usuario))
        else:
            print('Jogo terminou empatado. Computador com {} ponto(s). e Usuário com {} ponto(s).'.
                  format(pontuacao_computador, pontuacao_usuario))
        break

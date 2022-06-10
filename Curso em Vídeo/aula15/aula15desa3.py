""""Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""

from random import randint
print()
print('§' * 20)
print('JOGO DO PAR OU ÍMPAR')
print('§' * 20)
print()
vitorias = 0
while True:
    numero_usuario = int(input('Digite um número entre 0 e 5: '))
    numero_computador = randint(0, 5)
    soma = numero_usuario + numero_computador
    escolha_usuario = ' '
    while escolha_usuario not in 'PÍ':
        escolha_usuario = str(input('Digite [P]AR ou [Í]MPAR para jogar comigo: ')).strip().upper()[0]
    print(f'Você escolheu {numero_usuario} e eu escolhi {numero_computador}. A soma deu {soma}.')
    if escolha_usuario == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    elif escolha_usuario == 'Í':
        if soma % 2 == 1:
            print('Você venceu!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente!')
print(f'Game Over! Você ganhou {vitorias} vezes seguidas.')

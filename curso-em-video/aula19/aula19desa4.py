"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato."""

dados = {}
total_gols = []
contador = 1
dados['nome'] = str(input('Digite o nome do jogador: ')).strip().upper()
partidas = int(input(f'Digite quantas partidas {dados["nome"]} jogou: '))
for p in range(1, partidas+1):
    gols = int(input(f'Digite quantos gols foram feitos na partida {p}: '))
    total_gols.append(gols)
dados['gols'] = total_gols
dados['total'] = sum(total_gols)
print(dados)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for g in dados['gols']:
    print(f'Na partida {contador}, fez ', end='')
    contador += 1
    print(f'{g} gols.')
print(f'Foi um total de {dados["total"]} gols.')

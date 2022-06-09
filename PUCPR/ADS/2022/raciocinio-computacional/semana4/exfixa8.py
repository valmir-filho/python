# Unidade 04: Listas.
"""Exercício de fixação 8: Crie um programa que solicite o nome de quatro times de futebol e simule partidas de forma
que cada time jogue uma vez com os outros três. Na partida, deve perguntar quantos gols fez cada time e somar as
devidas pontuações. Ao final, deve dizer quais times foram campeões, visto que pode haver empate em pontuação.
Observação: vitória vale 3 pontos para o vencedor, empate vale 1 ponto para cada time e derrota não soma pontos."""

times = []
tabela = [0, 0, 0, 0]
for _ in range(4):
    time = input('Digite o nome de um dos times: ')
    times.append(time)
for i in range(3):
    for j in range(i + 1, 4):
        print('Jogo:', times[i], 'x', times[j])
        gols1 = int(input('Gols do ' + times[i] + ': '))
        gols2 = int(input('Gols do ' + times[j] + ': '))
        if gols1 > gols2:
            tabela[i] += 3
        elif gols1 < gols2:
            tabela[j] += 3
        else:
            tabela[i] += 1
            tabela[j] += 1
print('*** Pontuação dos Times ***')
for i in range(4):
    print(times[i] + ": ", tabela[i])
maior = max(tabela)
print('****** Time Campeão ******')
for i in range(4):
    if tabela[i] == maior:
        print(times[i])

"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição na tabela está o time da Chapecoense."""

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro',
         'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco da Gama',
         'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
print(f'Os 5 primeiros colocados são: {times[0:5]}.')
print(f'Os últimos 4 colocados são: {times[-4:]}.')
print(f'Times em ordem alfabética: {sorted(times)}.')
print(f'O time Chapecoense está na posição nº {times.index("Chapecoense")+1}.')

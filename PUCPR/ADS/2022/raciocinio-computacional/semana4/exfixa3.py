# Unidade 04: Listas.
"""Exercício de fixação 3: Crie um programa que leia as temperaturas médias de cada mês do ano e as armazene em uma
lista. Use outro vetor para guardar e exibir, quando necessário, o nome dos meses do ano; calcule a média anual de
temperatura e informe quais meses ficaram acima da média anual."""

temp_media = []
meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
for mes in meses_ano:
    temp = float(input('Informe a temperatura média do mês de ' + mes + ': '))
    temp_media.append(temp)
media_anual = sum(temp_media) / 12
print('A média anual é: {:.2f}'.format(media_anual), 'ºC')
print('Os meses com temperatura acima da média anual são: ')
for i in range(12):
    if temp_media[i] > media_anual:
        print(meses_ano[i], ':', temp_media[i], 'ºC')

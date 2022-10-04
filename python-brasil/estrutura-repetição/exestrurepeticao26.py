"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 26: Em uma eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para
cada eleitor votar e ao final mostrar o número de votos de cada candidato."""

mito = lula = primo = nulo = 0
opcoes_voto = (1, 2, 3)
while True:
    num_eleitores = int(input('Informe o número de eleitores: '))
    if num_eleitores <= 0:
        print('Valor inválido! Digite um númer maior que 0.')
    else:
        break
print('🇧🇷' * 13)
print('''RELAÇÃO DE CANDIDATOS
1) Mito
2) Lula Molusco
3) Primo''')
print('🇧🇷' * 13)
for i in range(1, num_eleitores + 1):
    print('Eleitor ' + str(i) + '.')
    voto = int(input('Vote em um dos 3 candidatos, digitando o seu número correspondente: '))
    if voto == 1:
        print('Você votou no Mito.')
        mito += 1
    elif voto == 2:
        print('Você votou no Lula Molusco.')
        lula += 1
    elif voto == 3:
        print('Você votou nulo.')
        primo += 1
    else:
        print('Você votou nulo.')
        nulo += 1
print('🏆' * 13)
print('RESULTADO DAS ELEIÇÕES')
print('🏆' * 13)
print(f'O candidato Mito recebeu {mito} votos.')
print(f'O candidato Lula Molusco recebeu {lula} votos.')
print(f'O candidato Primo recebeu {primo} votos.')
print(f'{nulo} votos foram nulos.')

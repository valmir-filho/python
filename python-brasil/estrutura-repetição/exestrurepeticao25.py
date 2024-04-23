"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 25: Faça um programa que peça para n pessoas a sua idade. Ao final, o programa devera verificar se a média de
idade da turma varia entre 0 e 25, 26 e 60 e maior que 60. Então, dizer se a turma é jovem, adulta ou idosa, conforme a
média calculada."""

idades = []
contador = 0
while True:
    idade = int(input('Informe a idade: '))
    idades.append(idade)
    contador += 1
    continuar = str(input('Deseja continuar informando idades? (S=sim/N=não): ')).strip().upper()
    if continuar == 'N':
        media = sum(idades)/contador
        print(f'A média de idade da turma é de: {media:.1f} anos.')
        if media <= 25:
            print('A turma é formada por jovens.')
        elif 26 < media <= 60:
            print('A turma é formada por adultos.')
        else:
            print('A turma é formada por idosos.')
        break

"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 27: Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e
a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos."""

quant_turmas = 0
media = []
while quant_turmas <= 0:
    quant_turmas = int(input('Informe a quantidade de turmas: '))
    if quant_turmas <= 0:
        print('Valor inválido! Digite um número maior que 0.')
for t in range(1, quant_turmas+1):
    quant_alunos_turma = -1
    while quant_alunos_turma < 0 or quant_alunos_turma > 40:
        quant_alunos_turma = int(input(f'Informe o número de alunos da turma {t}: '))
        if quant_alunos_turma <= 0 or quant_alunos_turma > 40:
            print('Valor inválido! Digite um número maior que 0 e menor que 40.')
        else:
            media.append(quant_alunos_turma)
print(f'A quantidade média de alunos por turma é: {sum(media)/quant_turmas:.0f}.')

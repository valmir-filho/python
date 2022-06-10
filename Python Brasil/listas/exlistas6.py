"""Python Brasil
Lista de exercícios de listas.
Exercício 6: Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7,0."""

medias = []
contador = 0
for n in range(1, 11):
    nota1 = float(input(f'Digite a 1ª nota do aluno {n}: '))
    nota2 = float(input(f'Digite a 2ª nota do aluno {n}: '))
    nota3 = float(input(f'Digite a 3ª nota do aluno {n}: '))
    nota4 = float(input(f'Digite a 4ª nota do aluno {n}: '))
    media = (nota1+nota2+nota3+nota4)/4
    medias.append(media)
for media in medias:
    if media >= 7:
        contador +=1
print(f'{contador} alunos possuem nota igual ou superior a 7,0.')


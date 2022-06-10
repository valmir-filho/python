"""Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a
média atingida:
— Média abaixo de 5.0: Reprovado;
— Média entre 5.0 e 6.9. Recuperação;
— Média 7.0 ou superior. Aprovado."""

nota1 = float(input('Informe a nota 1: '))
nota2 = float(input('Informe a nota 2: '))
media = (nota1 + nota2) / 2
print('A sua média é: {:.1f}'.format(media))
if media < 5:
    print('Você está reprovado.')
elif 5 <= media <= 6.9:
    print('Você está em recuperação.')
else:
    print('Você está aprovado.')

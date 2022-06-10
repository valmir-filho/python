"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 14: Faça um programa que leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento     Conceito
Entre 9.0 e 10.0               A
Entre 7.5 e 9.0                B
Entre 6.0 e 7.5                C
Entre 4.0 e 6.0                D
Entre 4.0 e zero               E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E."""

nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
media = (nota1+nota2)/2
print('As suas notas são: {} e {}'.format(nota1,nota2))
print('A sua média é: {:.2f}'.format(media))
if 0 < media <= 4:
    print('A sua média está entre 0 e 4. Seu conceito é: "E"')
    print('Você está "REPROVADO"')
elif 4 < media <= 6:
    print('A sua média está entre 4 e 6. Seu conceito é: "D"')
    print('Você está "REPROVADO"')
elif 6 < media <= 7.5:
    print('A sua média está entre 6 e 7.5. Seu conceito é: "C"')
    print('Você está "APROVADO"')
elif 7.5 < media <= 9:
    print('A sua média está entre 7.5 e 9. Seu conceito é: "B"')
    print('Você está "APROVADO"')
else:
    print('A sua média está entre 9 e 10. Seu conceito é: "A"')
    print('Você está "APROVADO"')

"""Python Brasil
Lista de exercícios de estrutura de decisão.
Exercício 5: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média
alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez."""

import time
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digita a nota 2: '))
media = (nota1 + nota2)/2
print('Calculando a média...')
time.sleep(3)
print('A média entre a nota {} e a nota {} é: {:.2f}'.format(nota1,nota2,media))
print('Verificando a situação do aluno...')
time.sleep(3)
if media == 10:
    print('Você foi aprovado com distinção!!!')
elif media >= 7:
    print('Você foi aprovado!!!')
else:
    print('Você foi reprovado!!!')

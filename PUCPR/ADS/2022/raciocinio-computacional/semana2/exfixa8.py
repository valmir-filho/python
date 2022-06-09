# Unidade 02: Estruturas condicionais
# Exercício de fixação 8: Crie um programa que solicite ao usuário as quatro notas bimestrais de uma matéria
# e o número de faltas. Informe se o aluno foi aprovado ou reprovado, bem como o motivo, a saber:
# A média anual é 7.
# A disciplina possui 40 aulas.
# O mínimo exigido é 75% de presença.

nota1 = float(input("Informe a 1ª nota bimestral da disciplina: "))
nota2 = float(input("Informe a 2ª nota bimestral da disciplina: "))
nota3 = float(input("Informe a 3ª nota bimestral da disciplina: "))
nota4 = float(input("Informe a 4ª nota bimestral da disciplina: "))
faltas = int(input("Informe o número de faltas da disciplina: "))
media = (nota1+nota2+nota3+nota4)/4
print("A sua média é:", media)
if media >= 7 and faltas <= 10:
    print("Você está aprovado na disciplina!")
elif media < 7 and faltas <= 10:
    print("Você está reprovado por nota na disciplina!")
elif media >= 7 and faltas > 10:
    print("Você está reprovado por frequência na disciplina!")
else:
    print("Você está reprovado por nota e frequência na disciplina!")

# Unidade 02: Estruturas condicionais
# Exercício de fixação 5: Crie um programa que pergunte ao usuário em que turno trabalha.
# Formato da entrada: M – manhã, T – tarde ou N – noite. Mostre a mensagem “Bom dia!”, “Boa tarde!”, “Boa noite!”
# ou “Valor inválido!”, conforme o caso.

turno = str(input("Informe o seu salário turno de trabalho (M/T/N): "))
if turno == "M":
    print("Bom dia!")
elif turno == "T":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Informação inválida!")

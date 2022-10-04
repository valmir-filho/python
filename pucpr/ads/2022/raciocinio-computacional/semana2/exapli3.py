# Unidade 02: Estruturas condicionais
# Exemplo de aplicação 3: Elabore um programa que solicite ao usuário seu ano de nascimento e calcule sua idade.
# Para ser mais assertivo, também deve perguntar se o usuário já fez aniversário neste ano e analisar a influência
# dessa informação no cálculo da idade.

ano_atual = 2022
ano_nasc = int(input("Qual é o seu ano de nascimento? "))
aniversario = input("Você já fez aniversário neste ano (S/N)? ")
if aniversario == "S":
    print("A sua idade é", ano_atual - ano_nasc)
else:
    print("A sua idade é", (ano_atual - ano_nasc) - 1)

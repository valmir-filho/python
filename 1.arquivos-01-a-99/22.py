"""
Exercício: faça um programa que pergunte a hora ao usuário e, baseando-se na informação, exiba a saudação apropriada.

Dados: Bom dia (0-11 horas), Boa tarde (12-17 horas) e Boa noite (18-23 horas).
"""

entrada = input("Informe a hora atual (formato: HH): ")

if entrada.isdigit():
    hora_int = int(entrada)
    if 0 <= hora_int <= 11:
        print(f"Bom dia!")
    elif 12 <= hora_int <= 17:
        print(f"Boa tarde!")
    else:
        print(f"Boa noite")
else:
    print(f"Erro! O valor {entrada} não é um número inteiro.")

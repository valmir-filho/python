"""
Exercício: Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

entrada = input("Digite um número inteiro qualquer: ")

if entrada.isdigit():
    entrada_int = int(entrada)
    if entrada_int % 2 == 0:
        print(f"O número {entrada_int} é par.")
    else:
        print(f"O número {entrada_int} é ímpar.")
else:
    print(f"Erro! O valor {entrada} não é um número inteiro.")

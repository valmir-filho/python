"""
Exercício: faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva: "Seu nome é curto", se tiver entre 5 e 6 letras, escreva: "Seu nome é normal" e maior que 6 letras, escreva: "Seu nome é muito grande". 
"""

nome = input("Digite o seu primeiro nome: ")

if len(nome) <= 4:
    print("O seu nome é curto.")
elif len(nome) <= 6:
    print("O seu nome é normal.")
else:
    print("O seu nome é muito grande.")

# Unidade 05: Estrutura de dados: tuplas e dicionários
"""Exercício de fixação 4: Crie um programa que efetue o cadastro de produtos e preços. Caso o produto já exista,
deve perguntar se o usuário pretende atualizar o valor. Imprima o dicionário no fim do programa em formato de lista."""

produtos = {}
while True:
    nome = input("Digite o nome do produto: ")
    valor = float(input("Digite o valor do produto: "))
    if nome in produtos:
        if input(f"Produto já cadastrado com o valor {produtos[nome]}. Deseja alterar o valor? (s/n)") == "n":
            continue
    produtos[nome] = valor
    if input("Cadastrar um novo produto? (s/n)") == "n":
        break
for produto in produtos:
    print(f"{produto:>20}: R${produtos[produto]:.2f}")

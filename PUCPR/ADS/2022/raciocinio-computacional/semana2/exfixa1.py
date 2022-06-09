# Unidade 02: Estruturas condicionais
# Exercício de fixação 1: Crie um programa que pergunte a idade do usuário. Caso seja maior de idade,
# deve mostrar uma mensagem informando que pode se inscrever para fazer o teste para tirar a carteira de motorista.

idade = int(input("Digite a sua idade (em anos): "))
if idade >= 18:
    print("Você pode se inscrever para tirar a carteira de motorista")
else:
    print("Você não pode se inscrever para tirar a carteira de motorista")
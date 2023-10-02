# Operador ternário.

while True:
    try:
        print("Opções:")
        print("1 - Verificar se o número é par ou ímpar.")
        print("2 - Sair do programa.")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 2:
            print("Obrigado por utilizar o programa!")
            break
        else:
            numero = int(input("Digite um número qualquer: "))
            if numero % 2 == 0:
                print(f"{numero} é par.")
            else:
                print(f"{numero} é ímpar.")
    except ValueError:
        print("Erro! Digite um número inteiro.")

# while True:
#     try:
#         print("Opções:")
#         print("1 - Verificar se o número é par ou ímpar.")
#         print("2 - Sair do programa.")
#         opcao = int(input("Digite a opção desejada: "))
#         # Nesse if não é possível usar um operador ternário, pois temos mais de um comando
#         if opcao == 2:
#             print("Obrigado por utilizar o programa!")
#             break
#         else:
#             numero = int(input("Digite um número qualquer: "))
#             print(f"{numero} é par.") if numero % 2 == 0 else print(
#                 f"{numero} é ímpar.")
#     except ValueError:
#         print("Erro! Digite um número inteiro.")

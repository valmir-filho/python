primeiro_valor = input("Digite um valor qualquer: ")
segundo_valor = input("Digite outro valor qualquer: ")

if primeiro_valor > segundo_valor:
    print(
        f"O primeiro valor {primeiro_valor} é maior do que o segundo valor {segundo_valor}.")
elif primeiro_valor < segundo_valor:
    print(
        f"O primeiro valor {primeiro_valor} é menor do que o segundo valor {segundo_valor}.")
else:
    print(
        f"O primeiro valor {primeiro_valor} é igual ao segundo valor {segundo_valor}.")

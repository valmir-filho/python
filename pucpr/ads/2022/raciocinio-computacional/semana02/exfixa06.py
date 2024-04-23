# Unidade 02: Estruturas condicionais
# Exercício de fixação 6: Crie um programa que solicite ao usuário dois números e a operação que deseja executar
# entre eles. Mostre o resultado dessa operação no formato: num1 op num2 = resultado.

num1 = int(input("Digite o 1º número inteiro: "))
num2 = int(input("Digite o 2º número inteiro: "))
operacao = input("Escolha qual a operação deseja executar entre esses 2 números (+, -, /, *): ")
result = 0
if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "/":
    result = num1 / num2
elif operacao == "*":
    result = num1 * num2
else:
    operacao = "erro"
if operacao == "erro":
    print("Operação inválida!")
else:
    print(num1, operacao, num2, "=", result)

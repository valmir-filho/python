# Unidade 02: Estruturas condicionais
# Exemplo de aplicação 9: Elabore um programa que solicite três números diferentes ao usuário e informe qual deles é
# o menor (utilizar a cláusula elif do comando if).

num1 = float(input("Digite um 1º número qualquer: "))
num2 = float(input("Digite um 2º número qualquer diferente do 1º: "))
num3 = float(input("Digite um 3º número qualquer diferente dos outros 2 anteriores: "))
if num1 < num2 and num1 < num3:
    print("O 1º número é o menor")
elif num2 < num1 and num2 < num3:
    print("O 2º número é o menor")
else:
    print("O 3º número é o menor")

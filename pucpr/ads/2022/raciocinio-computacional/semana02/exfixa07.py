# Unidade 02: Estruturas condicionais
# Exercício de fixação 7: Crie um programa que pergunte o tamanho de três lados de um triângulo
# e informe o tipo de triângulo, a saber:
# Só será um triângulo quando a soma de dois lados sempre for maior que o terceiro lado.
# Equilátero: triângulo com todos os lados iguais.
# Isósceles: triângulo com dois lados iguais.
# Escaleno: triângulo com todos os lados diferentes.

lado1 = int(input("Digite o 1º lado do triângulo: "))
lado2 = int(input("Digite o 2º lado do triângulo: "))
lado3 = int(input("Digite o 3º lado do triângulo: "))
if lado1 + lado2 < lado3 or lado2 + lado3 < lado1 or lado1 + lado3 < lado2:
    print("Os lados informados não formam um triângulo!")
else:
    if lado1 == lado2 and lado1 == lado3:
        print("Os lados digitados formam um triângulo equilátero.")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Os lados digitados formam um triângulo isósceles.")
    else:
        print("Os lados digitados formam um triângulo escaleno.")

# Python Brasil
# Lista de exercícios de estrutura sequencial
# Exercício 11: Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

int1 = int(input("Informe um primeiro número inteiro: "))
int2 = int(input("Informe um segundo número inteiro: "))
real = float(input("Informe um número real: "))
print("O produto do dobro do primeiro número inteiro com a metade do segundo número inteiro é:",((int1*2)*(int2/2)))
print("A soma do triplo do primeiro número inteiro com o número real é",(int1*3+real))
print("O número real elevado ao cubo é:",(real**3))
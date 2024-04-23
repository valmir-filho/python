# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

print('=' * 24)
print('Analisador de triângulos')
print('=' * 24)
reta1 = float(input('Informe o comprimento da reta 1: '))
reta2 = float(input('Informe o comprimento da reta 2: '))
reta3 = float(input('Informe o comprimento da reta 3: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Esses 3 comprimentos de reta formam um triângulo')
else:
    print('Esses 3 comprimentos de reta não formam um triângulo')

""""Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos."""

pesos = []
for pessoas in range(1,6):
    peso = float(input('Informe o peso da pessoa {} (em kg): '.format(pessoas)))
    pesos.append(peso)
print('O maior peso é: {} kg e o menor peso é: {} kg.'.format(max(pesos), min(pesos)))

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor_metro = float(input('Digite um valor em metros: '))
print('{} metro(s) vale(m): {:.0f} centímetros e {:.0f} milímetros'.format(valor_metro, valor_metro*100, valor_metro*1000))

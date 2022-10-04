# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada km acima do limite.

velocidade = int(input('Digite a velocidade do carro (em km/h): '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você foi multado!!! A sua multa vai custar R${:.2f}'.format(multa))
else:
    print('Parabéns, você está dentro do limite de velocidade!!!')

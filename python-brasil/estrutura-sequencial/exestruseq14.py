"""Python Brasil
Lista de exercícios de estrutura sequencial.
Exercício 14: João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário do
seu trabalho. Toda a vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado
de São Paulo (50 quilos) deve pagar uma multa de R$4,00 por quilo excedente. João precisa que você faça um programa
que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além
do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens
adequadas."""

from time import sleep
peso = float(input('Informe o peso de peixes (em kg): '))
if peso > 50:
    print('\33[31mVocê excedeu a quantidade permitida de peixes em: {:.1f} quilos\33[m'.format(peso - 50))
    excesso = peso - 50
    multa = excesso * 4
    print('Calculando o valor da multa...')
    time.sleep(3)
    print('\33[;43mA sua multa será de R${:.2f}\33[m'.format(multa))
else:
    print('Parabéns!!! Você pescou de acordo com o permitido!!!')

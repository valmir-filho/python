"""Python Brasil
Lista de exercícios de estrutura sequencial.
Exercício 18: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
‘Internet’ (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

import time
tamanho_arquivo = float(input('\33[32mInforme o tamanho do arquivo para download (em MB): '))
velocidade_internet = float(input('Informe a velocidade do link da Internet (em Mbps): \33[m'))
tempo = (tamanho_arquivo / velocidade_internet) / 60
print()
print('Calculando o tempo aproximado para download...')
time.sleep(3)
print('\33[34mSeu arquivo será baixado em aproximadamente {:.2f} minutos\33[m'.format(tempo))

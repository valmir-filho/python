"""Faça um programa que tenha uma função chamada contador(), que receba 3 parâmetros: início, fim e passo e realize a
contagem. O seu programa tem que realizar 3 contagens através da função criada:
a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2:
c) Uma contagem personalizada."""

from time import sleep


def linha():
    print('∞' * 45)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    linha()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    contador = inicio
    sleep(3)
    if inicio < fim:
        while contador <= fim:
            print(f'{contador}', end=' ')
            contador += passo
            sleep(0.5)
        print('Fim!')
    else:
        contador = inicio
        while contador >= fim:
            print(f'{contador}', end=' ')
            contador -= passo
            sleep(0.5)
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Digite o valor inicial: '))
f = int(input('Digite o valor final: '))
p = int(input('Digite o passo: '))
contador(i, f, p)

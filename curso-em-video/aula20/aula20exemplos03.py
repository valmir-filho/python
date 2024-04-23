# Funções Python

def contador(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print(' Fim!')


contador(2, 4, 5, 6, 7, 8)
contador(2, 3, 7)
contador(1)
contador(1, 4)

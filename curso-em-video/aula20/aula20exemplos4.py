# Funções Python

def contador(*num):
    tam = len(num)
    print(f'Números digitados: {num}. Total igual a: {tam}.')


contador(2, 4, 5, 6, 7, 8)
contador(2, 3, 7)
contador(1)
contador(1, 4)

# Unidade 03: Estruturas de repetição.
# Exercício de fixação 1: Crie um programa que solicite ao usuário dez números, contando quantos são pares e quantos
# são ímpares e informando ao final essas informações.

cont_par = 0
cont_impar = 0
cont = 0
while cont <= 9:
    num = float(input('Digite o número ' + str(cont + 1) + ' de 10: '))
    cont = cont + 1
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
print('Dos 10 números digitados, {} são pares e {} são ímpares.'.format(cont_par, cont_impar))

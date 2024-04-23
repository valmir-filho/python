"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 19: Faça um programa que, aceite apenas números entre 0 e 1000, e determine o menor valor, o maior valor e a
soma dos valores."""

numeros = []
while True:
    n = float(input('Digite um número entre 0 e 1000: '))
    if n < 0 or n > 1000:
        print('Valor inválido! Digite novamente.')
    else:
        numeros.append(n)
        continuar = str(input('Deseja continuar digitando números? (S=sim/N=não): ')).strip().upper()
        if continuar == 'N':
            print(f'O menor valor digitado é: {min(numeros)}')
            print(f'O maior valor digitado é: {max(numeros)}')
            print(f'A soma dos valores digitados é: {sum(numeros)}')
            break

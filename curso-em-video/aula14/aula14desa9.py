""""Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar a digitar
ou não."""

numeros = []
while True:
    n = int(input('Digite um número inteiro qualquer: '))
    numeros.append(n)
    continuar = str(input('Deseja continuar a inserir números (S=sim/N=não): ')).strip().upper()
    if continuar == 'S':
        continue
    else:
        break
print('A média entre todos os números digitados é igual a {:.1f}.'.format(sum(numeros)/len(numeros)))
print('O maior número digitado é o {}.'.format(max(numeros)))
print('O menor número digitado é o {}.'.format(min(numeros)))

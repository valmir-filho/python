# Exemplos com a estrutura de repetição while.

# Vai imprimir de 1 a 10.
c = 1
while c <= 10:
    print(c, end='-')
    c += 1
print('Fim!')
print()

# Vai pedir números até o usuário digitar "0".
num = 1
while num != 0:
    num = int(input('Digite um número inteiro qualquer. Para finalizar, digite 0: '))
print('Fim')
print()

# Vai pedir números até o usuário digitar "S".
resposta = 'S'
while resposta == 'S':
    n = int(input('Digite um número qualquer: '))
    resposta = str(input('Quer continuar? (S=sim/N=não): ')).strip().upper()
print('Fim')
print()

# Vai pedir números até o usuário digitar "0" e vai dizer quais são pares e quais são ímpares.
num = 1
pares = impares = 0
while num != 0:
    num = int(input('Digite um número inteiro qualquer. Para finalizar, digite "0": '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print('Você digitou {} números pares e {} números ímpares.'.format(pares, impares))

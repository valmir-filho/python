# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 12: Elabore um programa que solicite um número inteiro ao usuário, em um intervalo entre 1 e 5.

while True:
    try:
        num = int(input('Digite um número inteiro entre 1 e 5: '))
        if 1 <= num <=5:
            break
        else:
            print('Erro! O número deve estar entre 1 e 5!')
    except ValueError:
        print('Erro! Você não digitou um número inteiro entre 1 e 5!')
print('Parabéns! Você digitou um número inteiro entre 1 e 5!')

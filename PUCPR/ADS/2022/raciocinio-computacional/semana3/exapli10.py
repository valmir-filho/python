# Unidade 03: Estruturas de repetição
# Exemplo de aplicação 10: Elabore um programa que solicite um número inteiro ao usuário, validando e imprimindo esse número.

while True:
    try:
        num = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Erro! Você não digitou um número inteiro!')
print('Parabéns! Você digitou um número inteiro!')


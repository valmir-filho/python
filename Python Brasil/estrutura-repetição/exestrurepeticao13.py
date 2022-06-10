"""Python Brasil
Lista de exercícios de estrutura de repetição.
Exercício 13: Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao
segundo número. Não utilize a função de potência da linguagem."""

print('-' * 29)
print('PROGRAMA GERADOR DE POTÊNCIAS')
print('-' * 29)
while True:
    base = float(input('Digite o valor da base: '))
    expoente = float(input('Digite o valor do expoente: '))
    print()
    print(f'O valor da potência é igual a: {base**expoente:.2f}.')
    print()
    continuar = str(input('Deseja continuar calculando potências? (S=sim/N=não): ')).strip().upper()
    print()
    if continuar == 'N':
        print('Obrigado por utilizar o programa 👏👏👏!')
        break

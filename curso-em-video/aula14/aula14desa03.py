""""Crie um programa que leia dois valores e mostre um menu na tela:
Digite [1] se quiser somar os 2 números;
Digite [2] se quiser multiplicar os 2 números;
Digite [3] se quiser saber qual é o maior número entre os 2 informados;
Digite [4] se quiser escolher novos números;
Digite [5] se quiser sair do programa."""

print()
n1 = float(input('Digite um 1º número qualquer: '))
n2 = float(input('Digite um 2º número qualquer: '))
opcao = 0
while opcao != 5:
    print()
    print('=' * 71)
    print('''MENU DE OPERAÇÕES
Digite [1] se quiser somar os 2 números.
Digite [2] se quiser multiplicar os 2 números.
Digite [3] se quiser saber qual é o maior número entre os 2 informados.
Digite [4] se quiser escolher novos números.
Digite [5] se quiser sair do programa.''')
    print('=' * 71)
    print()
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print()
        print('\33[34mA soma entre {} e {} é igual a: {}.\33[m'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print()
        print('\33[34mA multiplicação entre {} e {} é igual a: {}.\33[m'.format(n1, n2, n1*n2))
    elif opcao == 3:
        print()
        if n1 > n2:
            print('\33[34mO maior número entre {} e {} é: {}.\33[m'.format(n1, n2, n1))
        elif n2 > n1:
            print('\33[34mO maior número entre {} e {} é: {}.\33[m'.format(n1, n2, n2))
        else:
            print('\33[34mOs números são iguais.\33[m')
    elif opcao == 4:
        print()
        print('Informe os números novamente.')
        print()
        n1 = float(input('Digite um 1º número qualquer: '))
        n2 = float(input('Digite um 2º número qualquer: '))
    elif opcao == 5:
        print()
        print('\33[34mObrigado por utilizar o programa 😉!\33[m')
    else:
        print()
        print('\33[34mOpção inválida! Tente novamente.\33[m')

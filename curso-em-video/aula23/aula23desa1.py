"""Reescreva a função leiaInt() que fizemos em um dos desafios, incluindo agora, a possibilidade da digitação
de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[31mPrograma interrompido pelo usuário!\033[m')
            return 0
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro! Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print()
            print('\033[31mPrograma interrompido pelo usuário!\033[m')
            return 0
        else:
            return n


num1 = leia_int('Digite um número inteiro: ')
num2 = leia_float('Digite um número real: ')
print(f'O número inteiro digitado foi: {num1} e o número real digitado foi: {num2}.')

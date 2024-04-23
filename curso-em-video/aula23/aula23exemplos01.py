# Tratamento de exceções Python

try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    r = a /b
except (ValueError, TypeError):  # trata exceções do tipo: valor e tipo.
    print('Tivemos um problema com as informações que você digitou!')
except ZeroDivisionError:  # trata uma exceção de divisão por 0.
    print('Não é possivel uma divisão por 0!')
except KeyboardInterrupt:  # trata uma exceção de interrupção do processo, por parte do usuário.
    print('O usuário preferiu interromper o processo!')
except Exception as erro:  # permite escolher o tipo de exceção e apresenta qual é.
    print(f'O erro encontrado foi: {erro.__cause__}.')
else:
    print(f'O resultado da divisão é: {r:.2f}.')
finally:
    print('Obrigado por utilizar o programa! Volte sempre!')

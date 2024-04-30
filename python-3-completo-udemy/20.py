# Introdução ao try/except.

try:
    numero = input("Digite um número inteiro: ")
    numero_int = int(numero)
    print(f"O número digitado foi: {numero}.")
except ValueError:
    print("Erro! O valor informado não é um número inteiro.")
# except Exception as error:
#     print(f"Erro! Ocorreu a seguinte exceção: {str(error)}.")
finally:  # Sempre será executado
    print("Fim da execução do código!")

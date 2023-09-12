# Introdução ao try/except

try:
    numero = input("Digite um número inteiro: ")
    numero_int = int(numero)
    print(f"O número digitado foi: {numero}.")
except ValueError:
    print("Erro! o valor informado não é um número inteiro!")
except Exception as e:
    print(f"Erro! Ocorreu a seguinte exceção: {str(e)}.")
finally:
    print("Fim da execução do código!")

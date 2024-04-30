# Calculadora com while.

while True:
    try:
        primeiro_numero = float(input("Digite o primeiro número: "))
        segundo_numero = float(input("Digite o segundo número: "))
        operador = input("Digite o operador (+, -, *, /) ou 'sair' para encerrar: ")
        
        if operador.lower() == "sair":
            break
        elif operador not in "+-*/" or len(operador) > 1:
            print("Erro! Operador inválido.")
        else:
            if operador == "+":
                resultado = primeiro_numero + segundo_numero
                print(
                    f"A soma entre {primeiro_numero} e {segundo_numero} é: {resultado}.")
            elif operador == "-":
                resultado = primeiro_numero - segundo_numero
                print(
                    f"A subtração entre {primeiro_numero} e {segundo_numero} é: {resultado}.")
            elif operador == "*":
                resultado = primeiro_numero * segundo_numero
                print(
                    f"A multiplicação entre {primeiro_numero} e {segundo_numero} é: {resultado}.")
            elif operador == "/":
                if segundo_numero == 0:
                    print("Erro! Não é possível dividir por zero.")
                else:
                    resultado = primeiro_numero / segundo_numero
                    print(
                        f"A divisão entre {primeiro_numero} e {segundo_numero} é: {resultado:.2f}")
    except ValueError:
        print("Erro! Certifique-se de digitar um número válido.")

print("Calculadora encerrada!")

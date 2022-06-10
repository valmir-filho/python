# Parâmetros opcionais

def somar(a, b, c=0):  # Nesse caso, o "c" entra como um parâmetro opcional, pois se não for informado o valor de "c", ele irá receber o valor "0".
    s = a+b+c
    print(f'A soma vale {s}.')


somar(3, 2, 5)
somar(8, 10)  # Não precisei informar o valor de "c", pois ele está como um parâmetro opcional.

# Uso de funções com retorno ("return").

def somar(a=0, b=0, c=0):
    s = a+b+c
    return s


r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)

print(f'As somas deram: {r1}, {r2} e {r2}.')

# Valores Falsy no Python.

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ""
numero_inteiro = 0
numero_flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def valores(valor):
    return "falsy" if not valor else "truthy"


print(f"{lista=}", valores(lista))
print(f"{dicionario=}", valores(dicionario))
print(f"{conjunto=}", valores(conjunto))
print(f"{tupla=}", valores(tupla))
print(f"{string=}", valores(string))
print(f"{numero_inteiro=}", valores(numero_inteiro))
print(f"{numero_flutuante=}", valores(numero_flutuante))
print(f"{nada=}", valores(nada))
print(f"{falso=}", valores(falso))
print(f"{intervalo=}", valores(intervalo))

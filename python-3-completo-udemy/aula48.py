# Iterável dentro de outro iterável.

dados = [["Maria", "Ana"], ["Helena"], [
    "Luiz", "Pedro", "João", (10, 20, 30, 40, 50)]]

print(dados)
print(dados[2][1])
print(dados[2][3][4])

for informacao in dados[2][3]:
    print(informacao)

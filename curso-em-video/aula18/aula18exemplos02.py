# Aplicações de variáveis compostas em Python.
# Listas em listas.

galera = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:  # Está a verificar na posição 1 (idade) quem é maior de 21.
        print(p[0])

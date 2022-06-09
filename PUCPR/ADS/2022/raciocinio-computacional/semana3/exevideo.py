# Estrutura de repetição.
for i in range(10):
    print (i)
# Estrutura de repetição.
cont = 0
while cont < 10:
    print(cont)
    cont = cont + 1
# O comando break interrompe a repetição.
for i in range(10):
    print(i)
    if i == 5:
        break
cont = 0
while cont < 10:
    print(cont)
    if cont == 5:
        break
    cont = cont + 1
# O comando continue, apenas continua após ser validada a condição.
for i in range(10):
    if i == 5:
        continue
    print(i)
# Comando pass.
while cont < 10:
    cont = cont + 1
    if cont == 5:
        pass
    print(cont)

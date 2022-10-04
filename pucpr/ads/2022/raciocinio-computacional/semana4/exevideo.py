# Unidade 04: Listas.
# Função para numerar a lista.
frutas = ['Laranja', 'Maçã', 'Banana', 'Morango', 'Manga', 'Abacaxi']
for i, item in enumerate(frutas):
    print(i, item)
print()

# Função para numerar e, em simultâneo, filtrar a lista.
for i, item in enumerate(frutas):
    if i < 3:
        print(i, item)
print()

# É possível definir o início do índice usando a função enumerate.
for i, item in enumerate(frutas, 100):
    print(i, item)
print()

# Separando os elementos pares dos ímpares.
pares = []
impares = []
for i, item in enumerate(frutas):
    if i % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)
print('Lista Pares')
for item in pares:
    print(item)
print()
print('Lista Ímpares')
for item in impares:
    print(item)

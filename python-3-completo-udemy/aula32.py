# While/else (recurso particular do Python).

string = "Palavra Aleatória!"

i = 0
while i < len(string):
    letra = string[i]
    print(letra)
    i += 1
else:
    print("Se o While não for interrompido, o else sempre será executado!")

# while i < len(string):
#     letra = string[i]
#     if letra == "t":
#         break
#     print(letra)
#     i += 1
# else:
#     print("Se o While não for interrompido, o else sempre será executado!")

# while i < len(string):
#     letra = string[i]
#     if letra == "s":
#         break
#     print(letra)
#     i += 1
# else:
#     print("Letra não encontrada!")

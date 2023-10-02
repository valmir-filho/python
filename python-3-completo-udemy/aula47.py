# Comandos "split" e "join" com strings e listas.

frase = "Aprender a programar com Python é a melhor maneira de iniciar na carreira de Programador."

# split
# Por padrão, o "split" vai usar o espaço para separas as palavras
lista_palavras = frase.split()
print(lista_palavras)
# lista_palavras = frase.split('a')
# print(lista_palavras)
# lista_palavras = frase.split('an')
# print(lista_palavras)

# for indice, frase1 in enumerate(lista_palavras):
#     print(lista_palavras[indice])

# join
frase = "-".join(lista_palavras)
print(frase)

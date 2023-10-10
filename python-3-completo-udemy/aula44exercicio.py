"""
Exercício: implemente um algoritmo em Python para manipular sua lista de filmes favoritos.

Especificações:

1) Crie uma lista vazia em Python;
2) Adicione o nome de 5 filmes na lista de favoritos;
3) O usuário deverá solicitar o nome de cada filme (usar o comando while);
4) Posteriormente imprima todos os filmes e sua posição na lista;
5) Para imprimir a lista utilizar o comando for em conjunto com a função enumerate().
"""

print("*** Top 5 Filmes Favoritos ***")

filmes_favoritos = []
contador = 1

while contador <= 5:
    filme = input(f"Digite o nome do filme favorito nº {contador}: ")
    filmes_favoritos.append(filme)
    contador += 1

print("Lista dos 5 filmes favoritos")
for indice, filme in enumerate(filmes_favoritos):

    print(indice+1, filme)

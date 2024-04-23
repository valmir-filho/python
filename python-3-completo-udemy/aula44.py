# Enumerate.

# Enumera iteráveis (índices)
relacao_nomes = "Maria", "José", "Pedro", "Ana"
relacao_enumerada_nomes = enumerate(relacao_nomes)
print(next(relacao_enumerada_nomes))
# print(list(enumerate(relacao_nomes)))
# print(list(enumerate(relacao_nomes, start=5)))

# for item in relacao_enumerada_nomes:
#     print(item)

# for item in enumerate(relacao_nomes):
#     print(item)

# for indice, nome in enumerate(relacao_nomes):
#     print(indice, nome)

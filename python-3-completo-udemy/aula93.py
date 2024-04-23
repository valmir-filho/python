# Crie um algoritmo para unir 2 listas. O resultado deve ser: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')].

cidades = ["Salvador", "Ubatuba", "Belo Horizonte"]
estados = ["BA", "SP", "MG", "RJ"]

# Verificação da menor lista
min_length = min(len(cidades), len(estados))

for i in range(min_length):
    resultado = [(cidades[i], estados[i])]
    print(resultado, end='')

# List comprehension para criar uma lista combinada
# resultado = [(cidades[i], estados[i]) for i in range(min_length)]

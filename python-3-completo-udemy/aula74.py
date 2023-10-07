"""
Mapeamento de dados em list comprehension.

Você pode usar list comprehensions para criar uma nova lista ao mapear (aplicar uma função) a cada elemento de uma sequência original. Isso é conhecido como mapeamento de dados usando List Comprehension. A ideia é aplicar uma expressão ou uma função a cada elemento da sequência original e criar uma nova lista com os resultados.
"""

# Exemplo 1
numeros = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in numeros]
print(quadrados)

# Exemplo 2
palavras = ["python", "é", "incrível"]
tamanhos = [len(word) for word in palavras]
print(tamanhos)

# Exemplo 3
temperaturas_celsius = [0, 25, 100]
temperaturas_fahrenheit = [(c * 9/5) + 32 for c in temperaturas_celsius]
print(temperaturas_fahrenheit)

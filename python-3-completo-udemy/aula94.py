"""
Função "zip()" no Python.

A função "zip()" no Python é usada para combinar elementos de duas ou mais sequências, como listas, tuplas ou outros iteráveis, em pares ordenados. Ela cria um iterador que produz tuplas contendo elementos correspondentes das sequências de entrada. A função "zip()" para de gerar elementos assim que uma das sequências de entrada se esgotar.
"""

nomes = ["Alice", "Bob", "Charlie"]
idades = [25, 30, 35]

for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos.")

"""
Observação: é importante notar que, se as sequências de entrada tiverem comprimentos diferentes, a função zip() produzirá pares apenas até o comprimento da sequência mais curta. Os elementos excedentes na sequência mais longa serão ignorados. 
"""

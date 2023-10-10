"""
Exercício.

1) Aumente o preço dos produtos em 10%.
2) Crie uma nova lista, usando deep copy, com esses novos preços.
3) Crie uma nova lista, usando deep copy, ordenando os produtos por nome decrescente (do maior para o menor).
4) Crie uma nova lista, usando deep copy, ordenando os produtos por nome crescente (do menor para o maior).
"""

import copy

produtos = [
    {"nome": "Produto 5", "preco": 10.00},
    {"nome": "Produto 1", "preco": 22.32},
    {"nome": "Produto 3", "preco": 10.11},
    {"nome": "Produto 2", "preco": 105.87},
    {"nome": "Produto 4", "preco": 69.90}
]


def aumento_10_porcento(lista_produtos):  # Acréscimo de 10% os produtos
    produtos_copiados = copy.deepcopy(lista_produtos)
    for produto in produtos_copiados:
        produto["preco"] *= 1.10
        # Limitando a 2 casas decimais após o ponto
        produto["preco"] = round(produto["preco"], 2)
    return produtos_copiados


produtos_com_aumento = aumento_10_porcento(produtos)

# Nova lista (usando deep copy) com os preços acrescidos de 10%
produtos_copiados = copy.deepcopy(produtos_com_aumento)

# Nova lista (usando deep copy) com os produtos em ordem decrescente por nome
produtos_nome_decrescente = copy.deepcopy(produtos)
produtos_nome_decrescente.sort(key=lambda x: x["nome"], reverse=True)

# Nova lista (usando deep copy) com os produtos em ordem crescente por nome
produtos_nome_crescente = copy.deepcopy(produtos)
produtos_nome_crescente.sort(key=lambda x: x["nome"])

print("∞∞∞ Produtos com aumento de 10% ∞∞∞")
for produto in produtos_com_aumento:
    print(f"{produto}")

print("\n∞∞∞ Produtos em ordem decrescente por nome ∞∞∞")
for produto in produtos_nome_decrescente:
    print(produto)

print("\n∞∞∞ Produtos em ordem crescente por nome ∞∞∞")
for produto in produtos_nome_crescente:
    print(produto)

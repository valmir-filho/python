"""
Exercício: implemente um algoritmo no Python para manipular uma lista de material escolar.

Especificações:

1) Criar duas estruturas de dicionário;
2) Armazenar 3 itens escolares no primeiro dicionário;
3) Criar o segundo dicionário vazio;
4) Os itens devem ser solicitados ao usuário (usar o comando while);
5) Código do produto (chave do dicionário);
6) Tipo do material (valor do dicionário);
7) Permita que o usuário adicione apenas 5 elementos na lista;
8) Atualizar o primeiro dicionário com o conteúdo do segundo (usar a função update());
9) Posteriormente imprima todos os elementos da lista (usar o comando for).
"""

lista_material_escolar_1 = {
    "produto1": "Caderno",
    "produto2": "Lápis",
    "produto3": "Borracha"
}

lista_material_escolar_2 = {}

contador = 0

while contador < 5:
    codigo_produto = input("Digite o código do produto: ")
    tipo_material = input("Digite o tipo de material: ")
    lista_material_escolar_2[codigo_produto] = tipo_material
    contador += 1

lista_material_escolar_1.update(lista_material_escolar_2)

print("∞∞∞ Lista de Material Escolar ∞∞∞")
for codigo, material in lista_material_escolar_1.items():
    print(f"Código: {codigo} - Tipo de Material: {material}.")

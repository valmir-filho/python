"""
Dicionários no Python.

Um dicionário é uma estrutura de dados em Python que armazena coleções de elementos de maneira associativa, ou seja, você pode armazenar pares de chave-valor. Cada elemento (item) em um dicionário consiste em uma chave única (índice) e um valor associado a essa chave. As chaves são imutáveis (podem ser: "str", "int", "float", "bool", "tuple"), enquanto os valores podem ser de qualquer tipo de dado (e são mutáveis).
"""

dados_pessoais_pessoa_1 = {
    "nome": "Valmir",
    "sobrenome": "Moro Conque Filho",
    "data_nascimento": "07/05/1979",
    "idade": 44,
    "estado_civil": "Casado",
    "enderecos": [
        {
            "tipo": "residencial",
            "logradouro": "Rua 29 de Junho",
            "numero": 267,
            "bairro": "Bacacheri",
            "complemento": "Torre 6 - Ap. 202",
            "cep": 82515396
        },
        {
            "tipo": "comercial",
            "logradouro": "Avenida Senador Souza Naves",
            "numero": 1715,
            "bairro": "Cristo Rei",
            "complemento": "",
            "cep": 80005040
        }
    ]
}

# dados_pessoais_pessoa_2 = dict(nome="Pedro", sobrenome="da Silva", endereco=[
#                                dict(tipo="residencial",
#                                     logradouro="Rua 29 de Junho", numero=23),
#                                dict(tipo="comercial",
#                                     logradouro="Rua Pio X", numero=50)
#                                ])

print(dados_pessoais_pessoa_1)
# print(dados_pessoais_pessoa_1["nome"])
# print(dados_pessoais_pessoa_1["enderecos"][0]["bairro"])
# print(dados_pessoais_pessoa_1["enderecos"][1]["cep"])

# for chave in dados_pessoais_pessoa_1:
#     print(chave)

# for valor in dados_pessoais_pessoa_1:
#     print(dados_pessoais_pessoa_1[valor])

# for dado in dados_pessoais_pessoa_1:
#     print(dado, dados_pessoais_pessoa_1[dado])

# Métodos úteis em dicionários no Python.

dados_pessoais = {
    "nome": "Valmir",
    "sobrenome": "Moro Conque Filho",
    "data_nascimento": "07/05/1979",
    "idade": 44,
    "estado_civil": "Casado",
    "endereco":
    {
        "logradouro": "Rua 29 de Junho",
        "numero": 267,
        "bairro": "Bacacheri",
        "complemento": "Torre 6 - Ap. 202",
        "cep": 82515396
    }
}

# get
# print(dados_pessoais.get("idade"))

# pop (apaga o item especificado pela chave)
# dados_pessoais.pop("estado_civil")
# print(dados_pessoais)

# popitem (apaga o último item do dicionário)
# dados_pessoais.popitem()
# print(dados_pessoais)

# update
# dados_pessoais.update({
#     "sexo": "masculino",
#     "casa_propria": True
# })

# dados_pessoais.update(sexo="masculino", altura="1.70")

print(dados_pessoais)

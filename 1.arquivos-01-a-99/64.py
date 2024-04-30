# Dicionários no Python.

dados_pessoais = {
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
print(dados_pessoais)
print()

# Adicionando uma nova chave ao dicionário
dados_pessoais["cpf"] = 11111111111
print(dados_pessoais)
print()

# Apagando uma chave do dicionário
del dados_pessoais["idade"]
print(dados_pessoais)

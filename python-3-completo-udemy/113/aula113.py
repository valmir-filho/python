# Criação de arquivo JSON no Python.

import json

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

with open("/Users/valmirfilho/Downloads/python-3-completo-udemy/aula113/aula113.json", "w") as arquivo:
    json.dump(
        dados_pessoais,
        arquivo,
        # ensure_ascii=False,
        indent=2
    )

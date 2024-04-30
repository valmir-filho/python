# Exportação de um arquivo JSON para o Python.

import json

with open("/Users/valmirfilho/Downloads/python-3-completo-udemy/aula114/aula114.json", "r") as arquivo:
    dados_pessoais = json.load(arquivo)
    print(dados_pessoais)
    print(dados_pessoais["idade"])

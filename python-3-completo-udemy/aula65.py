# Métodos úteis em dicionários no Python.

"""
Double underscore (ou dunder) methods.

Os métodos dunder em Python são métodos especiais que têm nomes que começam e terminam com dois underscores, como __init__, __str__, __add__, entre outros. Esses métodos são também conhecidos como métodos mágicos ou métodos especiais, e eles desempenham um papel fundamental na personalização do comportamento de objetos em Python.

Obs.: Métodos mais voltados para a orientação a objetos.
"""

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

# print(dados_pessoais.__len__())
# print(len(dados_pessoais))

# Retorno da chave do dicionário
# print(dados_pessoais.keys())

# Retorno do valor do dicionário
# print(dados_pessoais.values())

# Retorno da chave-valor do dicionário
# print(dados_pessoais.items())

# for chave, valor in dados_pessoais.items():
#     print(chave, valor)

"""
O método setdefault é usado em dicionários no Python para definir um valor padrão para uma chave, caso a chave não exista no dicionário. Se a chave já estiver presente no dicionário, o método setdefault não fará nenhuma alteração e apenas retornará o valor atual associado à chave. 
"""
# dados_pessoais.setdefault("doador_orgãos", True)
# print(dados_pessoais)

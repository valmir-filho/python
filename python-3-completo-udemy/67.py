# Shallow copy e deep copy em dicionários no Python.

"""
Shallow copy (cópia superficial): uma shallow copy de um dicionário cria uma nova cópia do dicionário original, mas os valores dentro do dicionário são referências aos mesmos objetos que estão no dicionário original. Isso significa que, se você modificar um valor dentro da cópia superficial, essa modificação será refletida no dicionário original e vice-versa.

Deep copy (cópia profunda): uma deep copy de um dicionário cria uma cópia totalmente independente do dicionário original, bem como de todos os objetos aninhados dentro dele. Isso significa que as alterações feitas na cópia profunda não afetam o dicionário original e vice-versa.
"""

# Exemplo de uma shallow copy
dicionario_original = {
    "chave_1": 1,
    "chave_2": 2,
    "chave_3": [3, 4]
}

copia_rasa_dicionario_original = dicionario_original.copy()

copia_rasa_dicionario_original["chave_1"] = 100
copia_rasa_dicionario_original["chave_3"].append(5)

# # Resultado: {'chave_1': 1, 'chave_2': 2, 'chave_3': [3, 4, 5]}
print(dicionario_original)
# # Resultado: {'chave_1': 100, 'chave_2': 2, 'chave_3': [3, 4, 5]}
print(copia_rasa_dicionario_original)

"""
Explicações:

O método copy() em dicionários cria uma cópia superficial (shallow copy) dos elementos do dicionário, o que significa que os valores do dicionário copiado são os mesmos objetos que os valores do dicionário original, a menos que sejam mutáveis (como listas, dicionários aninhados, etc.).

Quando você altera o valor da "chave_1" no "copia_dicionario_original", você está criando um novo objeto inteiro (um número) e associando-o à "chave_1" no "copia_dicionario_original". Isso não afeta o dicionário original, pois agora "chave_1" no "copia_dicionario_original" aponta para um objeto diferente do que "chave_1" no "dicionario_original".

Por outro lado, quando você faz "copia_dicionario_original["chave_3"].append(5), você está acessando a lista associada à "chave_3" e modificando essa lista (adicionando o valor 5 a ela). No entanto, essa lista é o mesmo objeto que a lista associada à "chave_3" no dicionário original, pois é uma cópia superficial. Portanto, as mudanças na lista são refletidas nos dois dicionários.
"""

# Exemplo de uma deep copy

# import copy
# dicionario_original = {
#     "chave_1": 1,
#     "chave_2": 2,
#     "chave_3": [3, 4]
# }

# copia_profunda_dicionario_original = copy.deepcopy(dicionario_original)

# copia_profunda_dicionario_original["chave_1"] = 100
# copia_profunda_dicionario_original["chave_3"].append(5)

# Resultado: {'chave_1': 1, 'chave_2': 2, 'chave_3': [3, 4]}
# print(dicionario_original)
# Resultado: {'chave_1': 100, 'chave_2': 2, 'chave_3': [3, 4, 5]}
# print(copia_profunda_dicionario_original)

"""
Explicações:

Neste caso, as alterações feitas no dicionário de cópia profunda não afetam o dicionário original.

Em resumo, quando você precisa criar uma cópia de um dicionário em Python, deve escolher entre uma shallow copy (cópia superficial), que compartilha os objetos internos com o original, ou uma deep copy (cópia profunda), que cria uma cópia independente de todos os objetos internos. A escolha depende das suas necessidades específicas em relação à manipulação dos dados.
"""

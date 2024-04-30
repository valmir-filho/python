"""
"dir", "hasattr" e "getattr"".

Em Python, "dir", "hasattr", e "getattr" são três funções relacionadas à introspecção de objetos e ao acesso dinâmico aos atributos de objetos. Aqui está uma explicação de cada uma delas:

1) dir(objeto)
- A função "dir" retorna uma lista de todos os nomes de atributos e métodos de um objeto.
- Ela pode ser usada para inspecionar os atributos disponíveis em um objeto, incluindo variáveis de instância e métodos.

2) hasattr(objeto, atributo):
- A função "hasattr" verifica se um objeto possui um atributo com o nome especificado.
- Ela retorna "True" se o atributo existir no objeto e "False" caso contrário.
- Pode ser útil para verificar a existência de um atributo antes de tentar acessá-lo.

3) getattr(objeto, atributo, valor_padrao):
- A função "getattr" obtém o valor de um atributo de um objeto.
- Se o atributo existir, ele retorna o valor desse atributo. Se o atributo não existir e um valor padrão for fornecido, ele retorna o valor padrão, caso contrário, gera uma exceção "AttributeError".
- Pode ser usado para acessar atributos dinamicamente com base em strings.

Em resumo, essas funções são úteis para examinar objetos e interagir com seus atributos de maneira dinâmica, tornando o código mais flexível e genérico. No entanto, tenha cuidado ao usar "getattr" e verifique a existência do atributo usando "hasattr" para evitar exceções desnecessárias.
"""

# Exemplo "dir"
lista = [1, 2, 3, 4, 5]
print(dir(lista))

# Exemplo "hasattr"
# dicionario = {"nome": "Valmir", "idade": 44, "altura": 1.70}
# print(hasattr(dicionario, "clear"))

# Exemplo "getattr"
# string = "Valmir"
# metodo = "lower"
# 
# if hasattr(string, metodo):
#     resultado = getattr(string, metodo)()
#     print(resultado)
# else:
#     print("Método não encontrado.")

"""
Função isinstance() no Python.

A função isinstance() no Python é usada para verificar se um objeto pertence a uma determinada classe ou tipo de dados. Ela retorna True se o objeto for uma instância da classe especificada ou de qualquer uma de suas subclasses, caso contrário, retorna False. A sintaxe geral da função isinstance() é a seguinte:

isinstance(objeto, classe_ou_tipo)

Aqui estão os parâmetros:

- objeto: o objeto que você deseja verificar.
- classe_ou_tipo: a classe ou o tipo de dados que você deseja verificar se o objeto é uma instância.

O uso de isinstance() é útil em muitos cenários, especialmente quando você deseja lidar com diferentes tipos de objetos de maneira condicional ou quando deseja garantir que um objeto seja do tipo correto antes de realizar certas operações com ele. No entanto, é importante usá-lo com cuidado e não abusar dele, pois pode tornar seu código menos legível se usado em excesso.
"""

lista = ["a", 1, 2, 4.4, True, [0, 1, 2], (1, 2)]
for item in lista:
    print(item, isinstance(item, int))
    # Passando 2 tipos ao mesmo tempo para verificação
    print(item, isinstance(item, (int, float)))

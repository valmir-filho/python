"""
Getter e Setter no Python.

No Python, os "getter" e "setter" são métodos usados para acessar e modificar os atributos de uma classe de forma controlada. Eles são comumente usados para
encapsular os atributos de uma classe e impor regras ou lógica durante a leitura (getter) e escrita (setter) desses atributos. Vamos explicar o conceito de
getter e setter no Python:

Getter:

- Um getter é um método que permite obter o valor de um atributo privado de uma classe.
- É usado para fornecer acesso controlado aos atributos da classe, tornando-os somente leitura.
- O nome do método getter geralmente começa com "get" seguido do nome do atributo, em minúsculas.

Setter:

- Um setter é um método que permite definir o valor de um atributo privado de uma classe.
- É usado para fornecer acesso controlado aos atributos da classe, tornando-os somente escrita.
- O nome do método setter geralmente começa com "set" seguido do nome do atributo, em minúsculas.

Os getters e setters são úteis quando você deseja controlar o acesso aos atributos de uma classe, adicionar lógica de validação ou realizar ações específicas
durante a leitura e escrita desses atributos. No entanto, no Python, a convenção é usar propriedades para implementar getters e setters de forma mais elegante,
permitindo que você acesse atributos como se fossem variáveis comuns, mas com lógica de controle por trás.
"""

# Exemplo de Getter


class Pessoa:
    def __init__(self, nome):
        self.__nome = nome  # Atributo privado

    def get_nome(self):
        return self.__nome


pessoa = Pessoa("Alice")
nome = pessoa.get_nome()
print(nome)

# No exemplo acima, o atributo "__nome" é privado e só pode ser acessado através do método "get_nome".

# Exemplo de Setter


# class Pessoa:
#     def __init__(self, nome):
#         self.__nome = nome  # Atributo privado

#     def set_nome(self, novo_nome):
#         if len(novo_nome) >= 3:
#             self.__nome = novo_nome

#     def get_nome(self):
#         return self.__nome

# pessoa = Pessoa("Alice")
# pessoa.set_nome("Bob")
# print(pessoa.get_nome())

# pessoa.set_nome("A")  # Não alterará o nome, pois a condição não será satisfeita
# print(pessoa.get_nome())

"""
Neste exemplo, o método "set_nome" permite alterar o valor do atributo "__nome", mas apenas se a condição (no caso, que o nome tenha pelo menos 3 caracteres)
for satisfeita.
"""

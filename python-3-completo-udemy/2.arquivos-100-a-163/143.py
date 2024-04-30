"""
Métodos "__repr__" e "__str__" no Python.

Os métodos "__repr__" e "__str__" são "Special Methods" (também conhecidos como "Dunder Methods") em Python que permitem personalizar a representação de uma classe
em forma de string.

Cada um deles serve a um propósito ligeiramente diferente:

"__str__":

- O método "__str__" é usado para retornar uma representação de string legível para humanos do objeto.
- É chamado automaticamente quando você tenta converter um objeto em uma string usando a função "str()".
- É uma boa prática fornecer uma representação clara e amigável do objeto, de modo que os usuários possam entender facilmente o que o objeto representa.

"__repr__":

- O método "__repr__" é usado para retornar uma representação de string que deve ser suficientemente precisa para reconstruir o objeto, se possível.
- É chamado automaticamente quando você usa a função "repr()" em um objeto, que é útil para depuração e inspeção de objetos.
- A representação retornada pelo método "__repr__" deve ser válida em Python e geralmente é usada para fornecer informações detalhadas sobre o estado do objeto.

Lembrando que a implementação de "__str__" é opcional, mas a implementação de "__repr__" é recomendada, pois pode ser muito útil para depurar e inspecionar objetos.
Se "__str__" não estiver definido, o Python usará o método "__repr__" como substituto quando a conversão para string for necessária.
"""

# Exemplo de uso de "__str__"


class Pessoa1:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome}, {self.idade} anos de idade.'


pessoa = Pessoa1("Alice", 30)
print(str(pessoa))  # Chama automaticamente __str__

# Exemplo de uso de "__repr__"


class Pessoa2:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'Pessoa("{self.nome}", {self.idade}).'


pessoa = Pessoa2("Bob", 25)
print(repr(pessoa))  # Chama automaticamente __repr__

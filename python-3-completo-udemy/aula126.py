"""
@property no Python.

O @property no Python é um decorador que permite que você defina um método de acesso especial chamado "getter" para um atributo de classe. O uso do @property é uma técnica que ajuda a tornar o código mais limpo, a evitar o acesso direto a atributos e a fornecer um controle mais sofisticado sobre a leitura de atributos. Isso é útil quando você deseja executar alguma lógica personalizada ao acessar um atributo, como validações ou cálculos.
"""


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade >= 0:
            self._idade = nova_idade
        else:
            raise ValueError("Idade não pode ser negativa.")

    @idade.deleter
    def idade(self):
        print("A idade foi deletada.")
        del self._idade


# Criando uma instância da classe
pessoa = Pessoa("Alice", 30)

# Usando o getter para acessar o atributo "nome"
print(pessoa.nome)

# Usando o getter para acessar o atributo "idade"
print(pessoa.idade)

# Usando o setter para modificar o atributo "idade"
pessoa.idade = 35

# Usando o deleter para deletar o atributo "idade"
del pessoa.idade

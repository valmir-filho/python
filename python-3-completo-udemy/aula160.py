"""
Dataclasses com métodos, property e setter no Python.

As "dataclasses" no Python são uma forma eficiente e limpa de criar classes que armazenam dados. Elas facilitam a criação de classes que, principalmente, têm o
propósito de armazenar dados, automatizando a criação de métodos especiais como "__init__", "__repr__", e "__eq__".
"""

# Definindo uma Data Class Básica: primeiro, importamos o decorador "dataclass" do módulo "dataclasses".

from dataclasses import dataclass


@dataclass
class Pessoa1:
    nome: str
    idade: int


# Adicionando Métodos: podemos adicionar métodos como em qualquer outra classe.


@dataclass
class Pessoa2:
    nome: str
    idade1: int

    def saudacao(self):
        return f"Olá, meu nome é {self.nome}!"


# Usando "property" e "setter": para adicionar uma propriedade com um getter e um setter, você pode fazer o seguinte:


@dataclass
class Pessoa3:
    nome: str
    _idade2: int = 0  # Usando um atributo privado para armazenar a idade

    @property
    def idade2(self):
        return self._idade2

    @idade2.setter
    def idade2(self, valor):
        if valor < 0:
            raise ValueError("Idade não pode ser negativa.")
        self._idade2 = valor


# Aqui, "idade2" é tratada como uma propriedade. O método decorado com "@property" funciona como um getter, e o método com "@idade2.setter" como um setter.

# Exemplo de Uso

pessoa = Pessoa2(nome="João", idade1=30)
print(pessoa.saudacao())  # Saída: Olá, meu nome é João!

pessoa.idade1 = 31  # Alterando a idade usando o setter
print(pessoa.idade1)  # Saída: 31

"""
Tentar definir uma idade negativa resultará em um erro, conforme definido no setter.

Essa é uma forma simplificada de como você pode combinar "dataclasses" com "property" e "setter" para criar classes de dados robustas e fáceis de manter em Python.
"""

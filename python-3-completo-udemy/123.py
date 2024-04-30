"""
@classmethod e factories no Python.

No Python, "classmethod" e "factories" são conceitos relacionados à programação orientada a objetos que permitem criar métodos que trabalham com a classe em vez de instâncias da classe.

- @classmethod (método de classe): um método de classe é um método que é associado à classe em vez de uma instância da classe. Isso significa que você pode chamar um método de classe diretamente na classe, em vez de em uma instância da classe. Para definir um método de classe em Python, você usa o decorador "@classmethod" antes da definição do método.

- Factory methods (métodos de fábrica): os "factory methods" são métodos de classe que são usados para criar instâncias de uma classe. Eles são úteis quando você deseja encapsular a lógica de criação de objetos em um método separado. Em Python, você pode implementar "factory methods" como métodos de classe que retornam uma instância da classe. Isso é frequentemente usado em design patterns como o Factory Method Pattern.

Em resumo, "@classmethod" é usado para criar métodos associados à classe em vez de instâncias, e "factory methods" são métodos de classe usados para criar instâncias da classe, geralmente encapsulando a lógica de criação de objetos. Ambos são úteis em diferentes situações de programação orientada a objetos em Python.
"""

# Exemplo de um @classmethod


class MinhaClasse:
    atributo = 0

    def __init__(self, valor):
        self.valor = valor

    @classmethod
    def metodo_de_classe(cls):
        cls.atributo += 1


# Uso do método de classe
MinhaClasse.metodo_de_classe()
print(MinhaClasse.atributo)

"""
Neste exemplo, "metodo_de_classe" é um método de classe e é chamado diretamente na classe "MinhaClasse" para modificar o atributo de classe atributo.
"""

# Exemplo de um factory method


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pessoa(cls, nome, idade):
        return cls(nome, idade)


# Usando o factory method
pessoa1 = Pessoa.criar_pessoa("Alice", 30)
pessoa2 = Pessoa.criar_pessoa("Bob", 25)

"""
Neste exemplo, o método "criar_pessoa" é um factory method que cria e retorna uma instância da classe Pessoa. Isso torna a criação de objetos mais flexível e encapsula a lógica de criação em um método separado.
"""
# __new__ de uma metaclass cria e retorna a classe em si no Python.


class MinhaMetaclasse(type):
    def __new__(cls, name, bases, attrs):
        # Crie e retorne a própria classe
        nova_classe = super(MinhaMetaclasse, cls).__new__(cls, name, bases, attrs)
        return nova_classe


class MinhaClasse(metaclass=MinhaMetaclasse):
    def __init__(self, valor):
        self.valor = valor

    def minha_metodo(self):
        return self.valor


# Crie uma instância da classe
obj = MinhaClasse(42)

# Acesse o método da classe
resultado = obj.minha_metodo()
print(resultado)

"""
Neste exemplo, a metaclasse MinhaMetaclasse define o método "__new__", que cria e retorna a própria classe. A classe MinhaClasse usa essa metaclasse ao definir
"metaclass=MinhaMetaclasse".

Ao criar uma instância da classe "MinhaClasse", ela aceita um valor que é passado para o construtor "__init__". O método minha_metodo da classe retorna esse valor.
Este é um exemplo simples para demonstrar que o método "__new__" da metaclasse cria e retorna a própria classe.
"""

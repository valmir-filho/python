"""
@staticmethod no Python.

No Python, os métodos estáticos ("static methods") são métodos definidos em uma classe que não dependem do estado da instância da classe. Em outras palavras, eles são métodos que não têm acesso aos atributos de instância e não podem modificar o estado da instância. Métodos estáticos são definidos usando o decorador "@staticmethod" antes da definição do método.

Aqui estão alguns pontos-chave sobre métodos estáticos em Python:

- Não requerem uma instância da classe: métodos estáticos podem ser chamados diretamente na classe, sem a necessidade de criar uma instância da classe. Eles não têm acesso aos atributos de instância, pois não recebem o parâmetro "self".

- Acesso à classe: no entanto, os métodos estáticos têm acesso à própria classe, pois eles recebem o parâmetro "cls", que é uma referência à classe em que estão definidos. Isso permite que você chame outros métodos estáticos ou acesse atributos de classe dentro do método.

- Não podem modificar o estado da instância: uma limitação importante dos métodos estáticos é que eles não podem modificar os atributos de instância, pois não têm acesso a "self". Eles são úteis para funções que não estão diretamente relacionadas ao estado das instâncias, mas ainda fazem sentido estar dentro da classe.

Os métodos estáticos são úteis em situações em que você deseja organizar funções relacionadas à classe, mas que não dependem do estado da instância. Eles são especialmente úteis quando você deseja criar funções utilitárias associadas a uma classe.
"""

# Exemplo


class MinhaClasse:
    atributo = 42

    def __init__(self, valor):
        self.valor = valor

    @staticmethod
    def metodo_estatico():
        return "Este é um método estático."

    @classmethod
    def metodo_de_classe(cls):
        return "Este é um método de classe."


# Usando métodos estáticos
resultado_estatico = MinhaClasse.metodo_estatico()
print(resultado_estatico)

# Usando métodos de classe
resultado_de_classe = MinhaClasse.metodo_de_classe()
print(resultado_de_classe)

"""
No exemplo, "metodo_estatico" é um método estático que não depende de instâncias e "metodo_de_classe" é um método de classe que pode acessar a classe, mas não pode acessar os atributos de instância diretamente.
"""

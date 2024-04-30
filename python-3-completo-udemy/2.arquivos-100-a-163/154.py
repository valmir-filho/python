# __call__ de uma metaclass cria e retorna a instância da classe no Python.


class MinhaMetaclasse(type):
    def __call__(cls, *args, **kwargs):
        # Crie e retorne uma instância da classe
        instancia = super(MinhaMetaclasse, cls).__call__(*args, **kwargs)
        return instancia


class MinhaClasse(metaclass=MinhaMetaclasse):
    def __init__(self, valor):
        self.valor = valor

    def minha_metodo(self):
        return self.valor


# Crie uma instância da classe
obj = MinhaClasse(42)

# Acesse o método da instância
resultado = obj.minha_metodo()
print(resultado)

"""
Neste exemplo, a metaclasse "MinhaMetaclasse" define o método "__call__", que é usado para criar e retornar uma instância da classe. A classe "MinhaClasse" usa essa
metaclasse ao definir "metaclass=MinhaMetaclasse".

Ao criar uma instância da classe "MinhaClasse" com "obj = MinhaClasse(42)", o método "__call__" da metaclasse é chamado, criando a instância da classe com o valor
passado como argumento. O método "minha_metodo" da instância pode ser acessado, retornando o valor definido no construtor.

Este é um exemplo simples para demonstrar como o método "__call__" da metaclasse pode ser usado para criar e retornar instâncias da classe.
"""

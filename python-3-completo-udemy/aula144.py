"""
Métodos "__new__" e "__init__" no Python.

Os métodos "__new__" e "__init__" são dois dos "Special Methods" (ou "Dunder Methods") mais importantes em Python e estão relacionados à criação e inicialização de
objetos em classes. Eles servem a propósitos distintos:

"__new__":

- O método "__new__" é responsável pela criação de uma nova instância de uma classe.
- Ele é chamado antes do método "__init__" e é o primeiro método a ser invocado quando um objeto é criado a partir de uma classe.
- A principal responsabilidade do método "__new__" é alocar memória para o objeto e retornar uma nova instância desse objeto. Normalmente, ele retorna uma instância
da classe, mas você pode personalizar esse comportamento se necessário.

"__init__":

- O método "__init__" é responsável pela inicialização de uma instância de uma classe após a instância ter sido criada por "__new__".
- Ele é chamado automaticamente após "__new__", quando um objeto é criado, e é usado para configurar atributos e realizar outras tarefas de inicialização.
- O método "__init__" recebe a instância recém-criada como seu primeiro argumento (por convenção, chamado de "self") e pode receber outros argumentos para
configurar o objeto.

Em resumo, "__new__" é responsável pela criação da instância, enquanto "__init__" é responsável pela sua inicialização. Geralmente, você não precisa definir o
método "__new__", a menos que tenha necessidades específicas, como controlar como as instâncias são criadas ou personalizar a inicialização. O método "__init__" é
comumente usado para configurar os atributos do objeto.
"""

# Exemplo de uso de "__new__"


class MinhaClasse1:
    def __new__(cls, *args, **kwargs):
        instance = super(MinhaClasse1, cls).__new__(cls)
        return instance

    def __init__(self, valor):
        self.valor = valor
        print('Método "__init__" chamado.')


obj = MinhaClasse1(42)  # Chama __new__ e, em seguida, __init__
print(obj.valor)  # Imprime 42

# Exemplo de uso de "__init__"


class MinhaClasse2:
    def __init__(self, valor):
        self.valor = valor
        print('Método "__init__" chamado.')


obj = MinhaClasse2(42)  # Chama __new__ e, em seguida, __init__
print(obj.valor)  # Imprime 42

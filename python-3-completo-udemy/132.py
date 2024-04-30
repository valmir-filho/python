""" 
super no Python.

A palavra-chave "super" no Python é usada para chamar métodos da classe base (superclasse) a partir de uma classe derivada (subclasse). Ela é comumente usada em
casos de herança quando a subclasse deseja estender ou modificar o comportamento de um método herdado da superclasse, ao mesmo tempo em que deseja executar o
código da superclasse.

A principal finalidade da palavra-chave "super" é manter o código mais organizado e evitar a duplicação de código. Quando você chama "super()", você está chamando
o método da superclasse que tem o mesmo nome dentro da subclasse. Isso é útil quando você deseja adicionar funcionalidade à implementação da superclasse, não
substituí-la completamente.

A sintaxe geral para usar "super" em Python é: "super().metodo_da_superclasse()"
"""

# Exemplo


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound."


class Dog(Animal):
    def speak(self):
        # Chama o método da superclasse e anexa o som específico do cão
        return f"{self.name} says Woof! - {super().speak()}"

dog = Dog("Buddy")
print(dog.speak())

"""
Neste exemplo, a classe "Dog" herda de "Animal" e substitui o método "speak()", mas também chama "super().speak()" para obter o som genérico da superclasse e
anexá-lo ao som específico do cão. Isso permite que a subclasse estenda o comportamento da superclasse em vez de reescrevê-lo inteiramente.
"""

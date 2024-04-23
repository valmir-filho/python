"""
No Python, o módulo "abc" (Abstract Base Classes) fornece o decorador "@abstractmethod" que é usado para declarar um método como um método abstrato em uma classe
abstrata. Um método abstrato é um método que é declarado, mas não contém uma implementação real na classe onde é declarado. Em vez disso, as subclasses devem
fornecer uma implementação concreta para esses métodos.
"""

# Exemplo

from abc import ABC, abstractmethod

class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

        
circle = Circle(5)
print(circle.area)

"""
Explicações:

- Criamos uma classe abstrata "Shape" que herda de "ABC" e contém um método abstrato "area" decorado com "@abstractmethod".

- Em seguida, criamos uma classe "Circle" que herda de "Shape" e fornece uma implementação concreta para o método "area". A classe "Circle" também define um
construtor que aceita o raio do círculo.

- A classe "Circle" é instanciada, e podemos chamar "circle.area" para calcular a área do círculo.

- O uso do decorador "@abstractmethod" em um método que também é um "@property" ou "@setter" é perfeitamente válido. Isso significa que você está exigindo que as
subclasses forneçam uma implementação concreta para esses métodos, independentemente de serem métodos de acesso ou de configuração.

No exemplo acima, o método "area" é um "@property" e um método abstrato ao mesmo tempo, o que significa que as subclasses devem fornecer uma implementação concreta para o método "area".
"""

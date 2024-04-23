"""
Abstração no Python.

A abstração é um conceito fundamental na programação orientada a objetos. Refere-se à prática de definir interfaces abstratas e esconder os detalhes de
implementação subjacentes. A abstração permite que você crie classes que representam conceitos de alto nível, sem se preocupar com os detalhes internos de como
esses conceitos são implementados. Isso ajuda na organização do código e na criação de código mais flexível e extensível.

No Python, você pode criar classes abstratas usando o módulo "abc" (Abstract Base Classes).
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length


"""
Neste exemplo, "Shape" é uma classe abstrata que define um método abstrato area(). As classes Circle e Square herdam de Shape e fornecem implementações concretas
para o método "area()". Isso cria uma abstração para formas geométricas, onde você pode chamar o método "area()" em qualquer objeto de uma classe derivada de
"Shape", independentemente de saber exatamente qual forma é. Isso facilita a adição de novos tipos de formas no futuro.
"""

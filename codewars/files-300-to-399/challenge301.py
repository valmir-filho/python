"""
Although shapes can be very different by nature, they can be sorted by the size of their area.

Task:

Create different shapes that can be part of a sortable list. The sort order is based on the size of their respective areas:

- The area of a Square is the square of its side;
- The area of a Rectangle is width multiplied by height;
- The area of a Triangle is base multiplied by height divided by 2;
- The area of a Circle is the square of its radius multiplied by π;
- The area of a CustomShape is given.

The default sort order of a list of shapes is ascending on area size:

- side = 1.1234;
- radius = 1.1234;
- base = 5;
- height = 2;
- shapes: List[Shape] = [Square(side), Circle(radius), Triangle(base, height)];
- shapes.sort().

Use the correct π constant for your circle area calculations: math.pi.
"""

import math
from typing import List


class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement the area method")

    def __lt__(self, other: 'Shape') -> bool:
        return self.area() < other.area()


class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return (self.base * self.height) / 2


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class CustomShape(Shape):
    def __init__(self, custom_area: float):
        self.custom_area = custom_area

    def area(self) -> float:
        return self.custom_area


# Exemplo de uso.
side = 1.1234
radius = 1.1234
base = 5
height = 2

shapes: List[Shape] = [
    Square(side),
    Circle(radius),
    Triangle(base, height),
    Rectangle(3, 4),
    CustomShape(10)
]

# Antes de ordenar.
print("Before sorting:")
for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area():.4f}")

# Ordenando.
shapes.sort()

# Depois de ordenar.
print("\nAfter sorting:")
for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area():.4f}")

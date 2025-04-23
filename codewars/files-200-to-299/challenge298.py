"""
Extend the Math object (JS) or module (Ruby and Python) to convert degrees to radians and viceversa.
The result should be rounded to two decimal points. Note that all methods of Math object are static.
"""


def degrees(rad):
    return f"{(rad * (180 / math.pi)):.2f}".rstrip('0').rstrip('.') + "deg"


def radians(deg):
    return f"{(deg * (math.pi / 180)):.2f}".rstrip('0').rstrip('.') + "rad"

# Criar um objeto "math" fake com pi e as funções.
math = type('math', (), {})()
math.pi = 3.141592653589793
math.degrees = degrees
math.radians = radians

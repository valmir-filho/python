"""
Task: Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
Division by zero should return an empty value.
"""


def remainder(a, b):
    # Identifica o menor e o maior valor.
    smaller = min(a, b)
    larger = max(a, b)
    
    # Verifica divisão por zero.
    if smaller == 0:
        return None  # Retorna "vazio" (None) conforme especificação.
    
    # Calcula e retorna o resto da divisão.
    return larger % smaller
  

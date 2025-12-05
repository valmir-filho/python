"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

# should return True.
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False. 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True.
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False.
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""


def same_structure_as(original, other):
    # Se um é lista e o outro não, já falha.
    if isinstance(original, list) != isinstance(other, list):
        return False
    
    # Se ambos não são listas, então são valores: estrutura é igual.
    if not isinstance(original, list):
        return True
    
    # Se são listas, devem ter o mesmo tamanho.
    if len(original) != len(other):
        return False
    
    # Verificar cada par de elementos recursivamente.
    return all(same_structure_as(o1, o2) for o1, o2 in zip(original, other))

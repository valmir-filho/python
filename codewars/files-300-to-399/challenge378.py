"""
The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that the two dimensions are different).

Can you translate this drawing into an algorithm?

You will be given two dimensions:

- a positive integer length;
- a positive integer width.

You will return a collection or a string (depending on the language; Shell bash, PowerShell, Pascal and Fortran return a string) with the size of each of the squares.

Notes:
lng == wdth as a starting case would be an entirely different problem and the drawing is planned to be interpreted with lng != wdth.

When the initial parameters are so that lng == wdth, the solution [lng] would be the most obvious but not in the spirit of this kata so,
in that case, return None/nil/null/Nothing or return {} with C++, [] with Perl, Raku.

In that case the returned structure of C will have its sz component equal to 0.

Return the string "nil" with Bash, PowerShell, Pascal and Fortran.
"""


def sq_in_rect(lng, wdth):
    # Se já é um quadrado perfeito, retorna None.
    if lng == wdth:
        return None
    
    result = []
    
    # Enquanto ainda tivermos retângulo.
    while lng > 0 and wdth > 0:
        # O lado do quadrado é sempre o menor dos dois.
        square = min(lng, wdth)
        result.append(square)
        
        # Atualiza o retângulo removendo o quadrado.
        if lng > wdth:
            lng -= wdth
        else:
            wdth -= lng
    
    return result

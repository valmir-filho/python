"""
The purpose of this kata is to write a program that can do some algebra.

Write a function expand that takes in an expression with a single, one character variable, and expands it.
The expression is in the form (ax+b)^n where a and b are integers which may be positive or negative, x is any single
character variable, and n is a natural number. If a = 1, no coefficient will be placed in front of the variable.
If a = -1, a "-" will be placed in front of the variable.

The expanded form should be returned as a string in the form ax^b+cx^d+ex^f... where a, c, and e are the coefficients
of the term, x is the original one character variable that was passed in the original expression and b, d, and f, are the
powers that x is being raised to in each term and are in decreasing order.

If the coefficient of a term is zero, the term should not be included.
If the coefficient of a term is one, the coefficient should not be included.
If the coefficient of a term is -1, only the "-" should be included.
If the power of the term is 0, only the coefficient should be included. If the power of the term is 1, the caret and power should be excluded.
"""

import re
from math import comb


def expand(expr):
    """
    Expande uma expressão binomial da forma (ax+b)^n.
    
    Args:
        expr (str): A expressão a ser expandida.
    
    Returns:
        str: A expressão expandida.
    """
    
    # Extrai os coeficientes 'a' e 'b', a variável 'x' e o expoente 'n'.
    match = re.match(r'\((-?\d*)(\D)([+-]\d+)\)\^(\d+)', expr)
    if not match:
        # Caso especial para quando 'a' é 1 ou -1.
        match = re.match(r'\((-?)(\D)([+-]\d+)\)\^(\d+)', expr)
        if match:
            a_str = match.group(1)
            x_var = match.group(2)
            b_val = int(match.group(3))
            n_exp = int(match.group(4))
            a_val = -1 if a_str == '-' else 1
        else:
            return "Erro: Formato da expressão inválido."
    else:
        a_str = match.group(1)
        x_var = match.group(2)
        b_val = int(match.group(3))
        n_exp = int(match.group(4))
        
        a_val = int(a_str) if a_str not in ('', '-') else (1 if a_str == '' else -1)

    # Se o expoente 'n' for 0, a expressão expandida é 1.
    if n_exp == 0:
        return '1'

    expanded_terms = []

    # Loop para gerar cada termo da expansão.
    for k in range(n_exp + 1):
        # Calcula o coeficiente binomial.
        binom_coeff = comb(n_exp, k)
        
        # Calcula o coeficiente total do termo.
        coeff = binom_coeff * (a_val**(n_exp - k)) * (b_val**k)
        
        # Ignora o termo se o coeficiente for 0.
        if coeff == 0:
            continue

        # Calcula o expoente da variável 'x'.
        x_exp = n_exp - k

        # Formata o termo.
        term_str = ""
        
        # Formata o coeficiente.
        if coeff == 1 and x_exp != 0:
            term_str += ""
        elif coeff == -1 and x_exp != 0:
            term_str += "-"
        else:
            term_str += str(coeff)

        # Formata a variável e seu expoente.
        if x_exp > 0:
            term_str += x_var
            if x_exp > 1:
                term_str += f"^{x_exp}"
        
        expanded_terms.append(term_str)

    # Junta todos os termos em uma única string, adicionando '+' se necessário.
    result = expanded_terms[0]
    for term in expanded_terms[1:]:
        if term.startswith('-'):
            result += term
        else:
            result += "+" + term
    
    return result

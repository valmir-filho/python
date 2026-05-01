""
Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

- A 1x1 matrix |a| has determinant a;

- A 2x2 matrix has determinant: a*d - b*c.

The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

For the 3x3 case, the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking
the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs.

The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then: det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor).
"""


def determinant(matrix):
    # Caso base: matriz 1x1.
    if len(matrix) == 1:
        return matrix[0][0]

    # Caso base: matriz 2x2.
    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

    # Caso geral: matriz NxN.
    det = 0
    for col in range(len(matrix)):
        # Criar a submatriz (minor).
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        # Alterna os sinais (+ - + - ...).
        cofactor = ((-1) ** col) * matrix[0][col]
        det += cofactor * determinant(minor)
    return det
 

"""
Given an m*n matrix M, calculate the determinant of all submatrices and return the greatest determinant of them.
"""

import numpy as np


def determinant(matrix):
    # Compute the determinant of a matrix using numpy.
    return int(round(np.linalg.det(matrix)))


def gdet(M):
    # Compute the greatest determinant among all submatrices of M.
    rows, cols = len(M), len(M[0])
    max_determinant = float('-inf')
    
    # Iterate over all possible top-left corners of submatrices.
    for start_row in range(rows):
        for start_col in range(cols):
            # Iterate over all possible submatrix sizes.
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    # Extract submatrix.
                    submatrix = [row[start_col:end_col] for row in M[start_row:end_row]]
                    # Compute determinant if submatrix is square.
                    if len(submatrix) == len(submatrix[0]):  # Check if square.
                        det = determinant(submatrix)
                        max_determinant = max(max_determinant, det)
    
    return max_determinant

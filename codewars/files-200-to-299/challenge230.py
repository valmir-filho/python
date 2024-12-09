"""
Given an N-dimensional cartesian space bound by N-dimensional planes (further "limits"),
and an N-dimensional linear function, find a point in this space at which this function
reaches its maximum possible value, and return this value.

Notes
- The space will always be finite;
- Each axis will always have a >= 0 limit which will not be included in the input;
- The origin of the space will always satisfy the given limits;
- Your solution should pass 10 cases with 150 variables and 150 limits as a performance test (the reference solution itself takes ~2000 ms to do so).
"""

import itertools
import numpy as np


def maximum_value(function, limits):
    # Extract the coefficients and constants from the limits.
    A = [limit[:-1] for limit in limits]
    b = [limit[-1] for limit in limits]
    
    # Combine axis bounds (x >= 0, y >= 0, etc.).
    num_vars = len(function)
    A += [[-1 if i == j else 0 for j in range(num_vars)] for i in range(num_vars)]
    b += [0] * num_vars
    
    # Find all combinations of constraints for intersections.
    vertices = []
    for combination in itertools.combinations(range(len(A)), num_vars):
        try:
            # Solve Ax = b for the current combination of constraints.
            subset_A = np.array([A[i] for i in combination])
            subset_b = np.array([b[i] for i in combination])
            point = np.linalg.solve(subset_A, subset_b)
            
            # Check if the point satisfies all constraints.
            if all(np.dot(A[i], point) <= b[i] + 1e-9 for i in range(len(A))):
                vertices.append(point)
        except np.linalg.LinAlgError:
            # Skip combinations that result in a singular matrix.
            pass
    
    # Evaluate the objective function at all feasible vertices.
    max_value = float('-inf')
    for vertex in vertices:
        value = sum(f * x for f, x in zip(function, vertex))
        max_value = max(max_value, value)
    
    return max_value

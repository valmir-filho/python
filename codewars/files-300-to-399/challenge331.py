"""
Do you know how to make a spiral? Let's test it!

Classic definition: A spiral is a curve which emanates from a central point, getting progressively farther away as it revolves around the point.

Your objective is to complete a function createSpiral(N) that receives an integer N and returns an NxN two-dimensional array with numbers 1 through NxN represented as a clockwise spiral.

Return an empty array if N < 1 or N is not int / number
"""


def create_spiral(n):
    if not isinstance(n, int) or n < 1:
        return []

    # Initialize an N x N matrix with zeros.
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    num = 1  # Start filling with number 1.
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1

    while row_start <= row_end and col_start <= col_end:
        # Fill the top row (from left to right).
        for j in range(col_start, col_end + 1):
            matrix[row_start][j] = num
            num += 1
        row_start += 1  # Move the top boundary down.

        # Fill the right column (from top to bottom).
        # This loop runs only if there are rows left to fill after the top row.
        for i in range(row_start, row_end + 1):
            matrix[i][col_end] = num
            num += 1
        col_end -= 1  # Move the right boundary left.

        # Fill the bottom row (from right to left).
        # Check if there's still a valid row to fill (row_start <= row_end).
        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                matrix[row_end][j] = num
                num += 1
            row_end -= 1  # Move the bottom boundary up.

        # Fill the left column (from bottom to top).
        # Check if there's still a valid column to fill (col_start <= col_end).
        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                matrix[i][col_start] = num
                num += 1
            col_start += 1  # Move the left boundary right.
            
    return matrix

"""
The function is given a rectangular grid of buildings height.
One can look from the left and from the top to the district and
see vertical and horizontal skylines. Each shorter building can
be increased in such a way such that the two skylines are not affected.
Determine the total maximum increase in all buildings whenever possible.
"""


def max_increase(grid):
    max_row = [max(row) for row in grid]
    max_col = [max(col) for col in zip(*grid)]
    
    total_increase = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_height = min(max_row[i], max_col[j])
            total_increase += max_height - grid[i][j]
    
    return total_increase

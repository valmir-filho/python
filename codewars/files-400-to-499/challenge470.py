"""
Write a function that will solve a 9x9 Sudoku puzzle.
The function will take one argument consisting of the 2D puzzle array,
with the value 0 representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable;
there will be no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

sudoku(puzzle)

# Should return

 [[5,3,4,6,7,8,9,1,2],
  [6,7,2,1,9,5,3,4,8],
  [1,9,8,3,4,2,5,6,7],
  [8,5,9,7,6,1,4,2,3],
  [4,2,6,8,5,3,7,9,1],
  [7,1,3,9,2,4,8,5,6],
  [9,6,1,5,3,7,2,8,4],
  [2,8,7,4,1,9,6,3,5],
  [3,4,5,2,8,6,1,7,9]]
"""


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    def is_valid(row, col, num):
        # linha.
        if num in puzzle[row]:
            return False

        # coluna.
        for r in range(9):
            if puzzle[r][col] == num:
                return False

        # bloco 3x3.
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if puzzle[r][c] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            puzzle[row][col] = num

                            if solve():
                                return True

                            puzzle[row][col] = 0

                    return False

        return True

    solve()
    return puzzle

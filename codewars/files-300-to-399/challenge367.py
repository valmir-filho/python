"""
In this kata you are expected to recover a scattered password in a (m x n) grid (you'll be given directions of all password pieces in the array).

The array will contain pieces of the password to be recovered, you'll get directions on how to get all the the pieces, your initial position in the array will be the character "x".

Heres what the array looks like:

[
  ["p", "x", "m"],
  ["a", "$", "$"],
  ["k", "i", "t"]
]

The given directions would consist of [left, right, up, down] and [leftT, rightT, upT, downT], the former would be used to move around the grid while the
latter would be used when you have a password to that direction of you.( E.g if you are in a position and the move to make is leftT it means theres a password
to the left of you, so take the value and move there).

So in the 2d array example above, you will be given the directions ["lefT", "downT", "rightT", "rightT"], making for the word "pa$$".

Remember you initial position is the character "x".

So you write the function getPassword(grid, directions) that uses the directions to get a password in the grid.

Another example:

grid = [
  ["a", "x", "c"],
  ["g", "l", "t"],
  ["o", "v", "e"]
];

directions = ["downT", "down", "leftT", "rightT", "rightT", "upT"]

getPassword(grid, directions) // => "lovet"

Once again, Your initial position is the character "x", so from the position of "x" you follow the directions given and get all pieces in the grid.
"""


def get_password(grid, directions):
    """
    Recupera uma senha de uma grade 2D seguindo uma série de direções.

    Args:
        grid: Uma lista de listas de strings, representando a grade.
        directions: Uma lista de strings, representando as direções a seguir.

    Returns:
        Uma string contendo a senha recuperada.
    """
    password = ""
    rows = len(grid)
    if rows == 0:
        return password
    cols = len(grid[0])
    
    # Encontra a posição inicial 'x'.
    current_row, current_col = -1, -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "x":
                current_row, current_col = r, c
                break
        if current_row != -1:
            break
            
    # Itera pelas direções.
    for direction in directions:
        next_row, next_col = current_row, current_col

        if direction == "up":
            next_row -= 1
        elif direction == "down":
            next_row += 1
        elif direction == "left":
            next_col -= 1
        elif direction == "right":
            next_col += 1
        elif direction == "upT":
            next_row -= 1
            if 0 <= next_row < rows and 0 <= next_col < cols:
                password += grid[next_row][next_col]
        elif direction == "downT":
            next_row += 1
            if 0 <= next_row < rows and 0 <= next_col < cols:
                password += grid[next_row][next_col]
        elif direction == "leftT":
            next_col -= 1
            if 0 <= next_row < rows and 0 <= next_col < cols:
                password += grid[next_row][next_col]
        elif direction == "rightT":
            next_col += 1
            if 0 <= next_row < rows and 0 <= next_col < cols:
                password += grid[next_row][next_col]

        # Atualiza a posição atual
        if 0 <= next_row < rows and 0 <= next_col < cols:
            current_row, current_col = next_row, next_col
            
    return password

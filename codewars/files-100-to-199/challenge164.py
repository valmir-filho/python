"""
You will be making a program that shows all positions a chess piece can go to.
The function has 2 parameters: the position on the chess board in the format a1
and a letter representing the piece. This will be K, Q, R, B, N for respectively
the King, Queen, Rook, Bishop and Knight.

This is what the matrix looks like for a queen in d3:

[[0,  0,  0,  1,  0,  0,  0,  0],
 [0,  0,  0,  1,  0,  0,  0,  1],
 [1,  0,  0,  1,  0,  0,  1,  0],
 [0,  1,  0,  1,  0,  1,  0,  0],
 [0,  0,  1,  1,  1,  0,  0,  0],
 [1,  1,  1, -1,  1,  1,  1,  1],
 [0,  0,  1,  1,  1,  0,  0,  0],
 [0,  1,  0,  1,  0,  1,  0,  0]]

Take a look at the test cases for some more examples: See https://en.wikipedia.org/wiki/Chess#Movement
for the movement rules of the pieces.
"""


def squares_covered(pos: str, piece: str):
    # Chessboard matrix: [row][column].
    m = [[0 for _ in range(8)] for _ in range(8)]

    # Convert position from 'a1' format to matrix indices.
    column = ord(pos[0]) - ord('a')  # Convert file (a-h) to 0-7.
    row = 8 - int(pos[1])  # Convert rank (1-8) to matrix row (7-0).

    # Place the piece at the specified position.
    m[row][column] = -1

  
    # Helper functions for each piece's movement.
    def king_moves(r, c):
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    m[nr][nc] = 1

  
    def queen_moves(r, c):
        rook_moves(r, c)
        bishop_moves(r, c)

  
    def rook_moves(r, c):
        for i in range(8):
            if i != r:
                m[i][c] = 1  # Vertical moves.
            if i != c:
                m[r][i] = 1  # Horizontal moves.

  
    def bishop_moves(r, c):
        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nr, nc = r, c
            while True:
                nr, nc = nr + dr, nc + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    m[nr][nc] = 1
                else:
                    break

  
    def knight_moves(r, c):
        for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                m[nr][nc] = 1

    # Determine piece movement.
    if piece == 'K':
        king_moves(row, column)
    elif piece == 'Q':
        queen_moves(row, column)
    elif piece == 'R':
        rook_moves(row, column)
    elif piece == 'B':
        bishop_moves(row, column)
    elif piece == 'N':
        knight_moves(row, column)

    return m

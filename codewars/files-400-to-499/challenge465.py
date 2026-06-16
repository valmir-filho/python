"""
Knight vs Rook

If you are not familiar with chess game you can learn more here.

You will be provided with a knight's and a rook's positions on the board.
Implement a function that tells us which piece can capture the other:

"Rook" if the rook captures the knight
"Knight" if the knight captures the rook
"None" otherwise

Check the test cases and Happy coding :)
"""


def knight_vs_rook(knight, rook):
    k_row, k_col = knight
    r_row, r_col = rook

    # Torre captura.
    if k_row == r_row or k_col == r_col:
        return "Rook"

    # Converte letras para números.
    dc = abs(ord(k_col) - ord(r_col))
    dr = abs(k_row - r_row)

    # Cavalo captura.
    if (dr, dc) in ((1, 2), (2, 1)):
        return "Knight"

    return "None"

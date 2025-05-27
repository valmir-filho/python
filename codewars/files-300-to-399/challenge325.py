"""
Given two different positions on a chess board, find the least number of moves it would take a knight to get from one to the other.
The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.
The knight is not allowed to move off the board. The board is 8x8.
For information on knight moves, see https://en.wikipedia.org/wiki/Knight_%28chess%29
For information on algebraic notation, see https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29
(Warning: many of the tests were generated randomly. If any do not work, the test cases will return the input, output, and expected output; please post them.)
"""

from collections import deque


def knight(p1, p2):
  
    # Conversão de notação algébrica para coordenadas (x, y).
    def algebraic_to_coord(pos):
        return ord(pos[0]) - ord('a'), int(pos[1]) - 1

    # Todos os 8 movimentos possíveis do cavalo.
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    start = algebraic_to_coord(p1)
    end = algebraic_to_coord(p2)

    if start == end:
        return 0

    # Fila para BFS: (posição, número de movimentos)
    queue = deque([(start, 0)])
    visited = set([start])

    while queue:
        (x, y), dist = queue.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if (nx, ny) == end:
                    return dist + 1
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), dist + 1))

    return -1  # Não deve acontecer se entrada for válida

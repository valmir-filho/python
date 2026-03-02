"""
Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships,
false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to
destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from
version to version. In this kata we will use Soviet/Russian version of the game.

Before the game begins, players set up the board and place the ships accordingly to the following rules:

- There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships;
- Each ship must be a straight line, except for submarines, which are just single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.

This is all you need to solve this kata. If you're interested in more information about the game, visit this link.
"""


def validate_battlefield(field):
    n = 10

    # Quick sanity: must be 10x10 of 0/1.
    if len(field) != n or any(len(row) != n for row in field):
        return False
    for row in field:
        for v in row:
            if v not in (0, 1):
                return False

    visited = [[False] * n for _ in range(n)]
    ships = []

    def neighbors8(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < n and 0 <= cc < n:
                    yield rr, cc

    def is_ship_cell(r, c):
        return field[r][c] == 1

    for r in range(n):
        for c in range(n):
            if not is_ship_cell(r, c) or visited[r][c]:
                continue

            # If this cell has diagonal contact with ANY ship cell, invalid (diagonal adjacency between different ships is forbidden; within a straight ship it also must never happen anyway, so it's always illegal.).
            for rr, cc in ((r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)):
                if 0 <= rr < n and 0 <= cc < n and is_ship_cell(rr, cc):
                    return False

            # Determine orientation (if any): horizontal or vertical or single.
            right = (c + 1 < n and is_ship_cell(r, c + 1))
            down = (r + 1 < n and is_ship_cell(r + 1, c))

            # Can't branch (an L / T shape).
            if right and down:
                return False

            cells = []

            if right:
                # Walk horizontally.
                cc = c
                while cc < n and is_ship_cell(r, cc):
                    # Vertical neighbor would make a bend/thickness -> invalid.
                    if (r - 1 >= 0 and is_ship_cell(r - 1, cc)) or (r + 1 < n and is_ship_cell(r + 1, cc)):
                        return False
                    cells.append((r, cc))
                    cc += 1
            elif down:
                # Walk vertically.
                rr = r
                while rr < n and is_ship_cell(rr, c):
                    # Horizontal neighbor would make a bend/thickness -> invalid.
                    if (c - 1 >= 0 and is_ship_cell(rr, c - 1)) or (c + 1 < n and is_ship_cell(rr, c + 1)):
                        return False
                    cells.append((rr, c))
                    rr += 1
            else:
                # Single cell ship (submarine candidate).
                cells = [(r, c)]

            # Mark visited and ensure no edge/corner contact with other ships outside this ship.
            ship_set = set(cells)
            for rr, cc in cells:
                if visited[rr][cc]:
                    return False
                visited[rr][cc] = True

            for rr, cc in cells:
                for ar, ac in neighbors8(rr, cc):
                    if is_ship_cell(ar, ac) and (ar, ac) not in ship_set:
                        # Touching another ship by edge or corner.
                        return False

            ships.append(len(cells))

    # Must match fleet: 1x4, 2x3, 3x2, 4x1.
    required = {4: 1, 3: 2, 2: 3, 1: 4}
    counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for size in ships:
        if size not in counts:
            return False
        counts[size] += 1

    return counts == required

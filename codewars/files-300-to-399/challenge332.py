"""
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

- Empty positions are marked ..
- Walls are marked W.
- Start and exit positions are empty in all test cases.
"""

import collections


def path_finder(maze: str) -> bool:
    maze_rows = maze.split('\n')
    N = len(maze_rows)

    # Basic validation for an NxN maze structure.
    # N must be at least 1. The first row's length must be N.
    if N == 0 or len(maze_rows[0]) != N:
        # Handles cases like maze="", maze="\n", or non-square inputs like ".\n..".
        # An empty string maze leads to N=1, maze_rows[0]="", len(maze_rows[0])=0. 0 != 1, so False.
        return False

    # Starting position is (0,0). Target position is (N-1, N-1).
    # The problem guarantees the start and end positions are empty ('.').
    
    queue = collections.deque([(0, 0)]) # Queue for BFS, initialized with start position
    visited = {(0, 0)}                  # Set to store visited coordinates

    while queue:
        r, c = queue.popleft()

        # Check if the current position is the target
        if r == N - 1 and c == N - 1:
            return True

        # Explore neighbors in cardinal directions: North, South, West, East
        # (dr, dc) are changes in row and column
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_r, next_c = r + dr, c + dc

            # Check if the neighbor is within maze boundaries
            if 0 <= next_r < N and 0 <= next_c < N:
                # Check if the neighbor is an empty path ('.')
                # and has not been visited yet
                if maze_rows[next_r][next_c] == '.' and (next_r, next_c) not in visited:
                    visited.add((next_r, next_c))
                    queue.append((next_r, next_c))
    
    # If the queue becomes empty and the target was not reached, no path exists
    return False

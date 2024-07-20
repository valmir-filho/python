"""
You are at position [0, 0] in maze NxN and you can only move in one of the four
cardinal directions (i.e. North, East, South, West). Return the minimal number
of steps to exit position [N-1, N-1] if it is possible to reach the exit from the
starting position. Otherwise, return false.

Empty positions are marked .. Walls are marked W. Start and exit positions are
guaranteed to be empty in all test cases.
"""

from collections import deque


def path_finder(maze):
    # Convert the maze string into a 2D list for easier manipulation.
    maze = maze.split('\n')
    N = len(maze)
    
    # Define the four possible directions (North, East, South, West).
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS initialization.
    queue = deque([(0, 0, 0)])  # (row, col, steps).
    visited = set((0, 0))
    
    while queue:
        x, y, steps = queue.popleft()
        
        # Check if we've reached the exit.
        if (x, y) == (N-1, N-1):
            return steps
        
        # Explore the four possible directions.
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check if the new position is within bounds and not a wall or visited.
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] == '.' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
    
    # If the queue is exhausted and we haven't reached the exit, return False.
    return False

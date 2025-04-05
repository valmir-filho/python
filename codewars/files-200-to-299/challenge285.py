"""
Given a set of 3 jugs of water that have capacities of a, b, and c liters,
find the minimum number of operations performed before each jug has x, y, and
z liters. Only jug C will start completely filled.
An operation is any of the following: A jug is filled, or water is poured from one
jug to another until one of the jugs is either empty or full.
Create a function that, given an array of jug capacities [A, B, C] and an goal state
array [x, y, z], returns the minimum number of operations needed to reach the goal state.
If there is no possible solution, return -1.
"""

from collections import deque


def solve(cap, goal):
    A, B, C = cap
    x, y, z = goal

    total = C  # Só o jarro C começa cheio.

    # Checagem básica de viabilidade.
    if x > A or y > B or z > C or x + y + z > total:
        return -1

    # BFS.
    queue = deque([(0, 0, C)])  # Estado inicial: apenas C cheio.
    visited = set([(0, 0, C)])
    operations = 0

    while queue:
        for _ in range(len(queue)):
            a, b, c = queue.popleft()
            if (a, b, c) == (x, y, z):
                return operations

            jugs = [a, b, c]
            capacities = [A, B, C]

            # Tenta todas as operações de transferência.
            for i in range(3):
                for j in range(3):
                    if i == j or jugs[i] == 0 or jugs[j] == capacities[j]:
                        continue
                    new_jugs = jugs[:]
                    transfer = min(jugs[i], capacities[j] - jugs[j])
                    new_jugs[i] -= transfer
                    new_jugs[j] += transfer
                    state = tuple(new_jugs)
                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

        operations += 1

    return -1

"""
🚀 Interstellar Escape Run 👽

“Fuel’s low, captain. The scanners show alien fleets nearby — we need a route, fast!”

You are the commander of one of humanity’s last surviving starships. Lost deep in hostile space, with limited fuel and alien patrols closing in,
your only hope is to navigate safely through a web of star systems to reach friendly territory before your engines run dry.

🧭 Task

You are given:

- A matrix representing the distances between star systems;
- A list of systems where aliens have been sighted — avoid these at all costs;
- The ship’s fuel capacity;
- A starting system and a destination system.

Your goal is to calculate the shortest safe route from start to destination without running out of fuel or entering alien-controlled systems.

Return:

- The fuel required (integer) if the destination is reachable and within fuel range;
- None if there is no safe route or if fuel is insufficient.

🧮 System Map Structure

The star map is represented as a square NumPy array (matrix), where each row and column correspond to a star system’s index.

For a matrix system_map:

- The element at system_map[i, j] represents the fuel cost (distance) to travel from system i to system j;
- If system_map[i, j] == 0, it means there is no direct route between those two systems;

Distances are bidirectional (symmetric): system_map[i, j] == system_map[j, i].

🔢 Example Matrix Visualization

system_map = np.array([
    [0, 5, 0, 2],
    [5, 0, 3, 0],
    [0, 3, 0, 1],
    [2, 0, 1, 0]
])

⚙️ Function Signature

def plot_course(system_map: np.ndarray, fuel: int, alien_sightings: list[int], start: int, destination: int) -> int | None:

Parameters
Name	          Type	     Description
system_map	    np.ndarray Square matrix of distances (lightyears) between systems. A value of 0 means no direct connection.
fuel	          int	       Maximum total distance your ship can travel.
alien_sightings	list[int]	 Indices of systems under alien control (cannot enter).
start	          int	       Index of your current system.
destination	    int	       Index of your target system.

🧠 Rules

- You may only travel along existing routes (> 0 distance);
- You cannot enter or pass through any system in alien_sightings;
- The route must not exceed the available fuel;
- If there are multiple valid routes, use the one with the lowest total distance;
- If start == destination, return 0.

🏁 Ready to Launch?

The stars await, captain. Can you guide your ship safely through hostile space and reach your destination before your fuel runs out?

Good luck, and may your jumps be precise! 🚀👽
"""

import numpy as np
import heapq


def plot_course(system_map, fuel, alien_sightings, start, destination):
    # Caso trivial.
    if start == destination:
        return 0

    n = len(system_map)
    blocked = set(alien_sightings)

    # Se início ou destino estiverem bloqueados, não há rota segura.
    if start in blocked or destination in blocked:
        return None

    # Dijkstra.
    distances = [float("inf")] * n
    distances[start] = 0
    heap = [(0, start)]  # (distância acumulada, nó).

    while heap:
        current_dist, node = heapq.heappop(heap)

        # Ignora entradas antigas da fila.
        if current_dist > distances[node]:
            continue

        # Se já ultrapassou o combustível, não vale continuar.
        if current_dist > fuel:
            continue

        # Chegou ao destino.
        if node == destination:
            return current_dist

        # Explora vizinhos.
        for neighbor in range(n):
            cost = system_map[node][neighbor]

            # Sem rota direta.
            if cost == 0:
                continue

            # Não pode entrar em sistema com alienígenas.
            if neighbor in blocked:
                continue

            new_dist = current_dist + cost

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))

    return None

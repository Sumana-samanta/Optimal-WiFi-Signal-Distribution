# Optimal-WiFi-Signal-Distribution
Determining an optimal path for WiFi signal propagation from a router to a target location while minimizing signal loss and avoiding obstacles.
#!/usr/bin/env python3
"""
WiFi Signal Distribution using A* Search Algorithm

Example:
  python3 wifi_signal_astar.py \
    --grid-size 5 \
    --start 0,0 \
    --goal 4,4 \
    --out result.txt
"""

from __future__ import annotations

import argparse
import heapq
from typing import List, Tuple


# -----------------------------
# Heuristic Function
# -----------------------------
def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -----------------------------
# A* Algorithm
# -----------------------------
def astar(grid: List[List[int]], start: Tuple[int, int], goal: Tuple[int, int]):
    rows, cols = len(grid), len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_cost = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            return reconstruct_path(came_from, current)

        x, y = current
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1:
                    continue

                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_set, (priority, (nx, ny)))
                    came_from[(nx, ny)] = current

    return None


# -----------------------------
# Path Reconstruction
# -----------------------------
def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]


# -----------------------------
# Grid Generator
# -----------------------------
def generate_grid(size: int):
    grid = [[0 for _ in range(size)] for _ in range(size)]

    # Example obstacles (fixed for demo)
    obstacles = [(0,3),(1,1),(1,3),(2,1),(3,2),(3,3)]
    for x, y in obstacles:
        if x < size and y < size:
            grid[x][y] = 1

    return grid


# -----------------------------
# Main Function
# -----------------------------
def main():
    parser = argparse.ArgumentParser(
        description="WiFi Signal Distribution using A* Search"
    )

    parser.add_argument("--grid-size", type=int, default=5)
    parser.add_argument("--start", type=str, required=True)
    parser.add_argument("--goal", type=str, required=True)
    parser.add_argument("--out", type=str, default="output.txt")

    args = parser.parse_args()

    start = tuple(map(int, args.start.split(",")))
    goal = tuple(map(int, args.goal.split(",")))

    grid = generate_grid(args.grid_size)

    print("Running A* Search for WiFi Signal Path...")
    path = astar(grid, start, goal)

    if path:
        print("Optimal Path Found:", path)
        with open(args.out, "w") as f:
            f.write("Path:\n")
            for p in path:
                f.write(f"{p}\n")
    else:
        print("No Path Found")


if __name__ == "__main__":
    main()

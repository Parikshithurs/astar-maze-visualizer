import numpy as np
import matplotlib.pyplot as plt
import heapq
import time

# -----------------------------
# Maze definition
# -----------------------------
maze = np.array([
    [5, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 6]
])

ROWS, COLS = maze.shape
start = (0, 0)
goal = (4, 4)

# -----------------------------
# Heuristic (Manhattan)
# -----------------------------
def h(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# -----------------------------
# Visualization
# -----------------------------
plt.ion()
fig, ax = plt.subplots()

def draw():
    ax.clear()
    ax.imshow(maze, cmap="tab10")
    ax.set_xticks([])
    ax.set_yticks([])
    plt.pause(0.2)

# -----------------------------
# A* Algorithm
# -----------------------------
def astar():
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # reconstruct path
            while current in came_from:
                current = came_from[current]
                if current != start:
                    maze[current] = 4
                    draw()
            return

        r, c = current
        if current != start:
            maze[current] = 3

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)

            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if maze[nr][nc] == 1 or maze[nr][nc] == 3:
                    continue

                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + h(neighbor, goal)
                    heapq.heappush(open_set, (f, neighbor))

                    if maze[nr][nc] == 0:
                        maze[nr][nc] = 2

        draw()

# -----------------------------
# Run
# -----------------------------
draw()
time.sleep(1)
astar()
plt.ioff()
plt.show()

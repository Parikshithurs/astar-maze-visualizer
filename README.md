# A* Maze Solver – Matplotlib Visualization

This project is a **visual implementation of the A\*** (A-star) **pathfinding algorithm** on a 2D grid maze using **Matplotlib**.

The maze layout, start position, and goal position are **defined in the code**, and the algorithm’s behavior is visualized step by step.  
The focus of this project is to understand how A\* explores the search space and how heuristics guide the algorithm toward the optimal path.

---

## 📂 File Structure

maze.py


- `maze.py` – contains:
  - grid (maze) definition
  - A\* algorithm logic
  - Matplotlib-based visualization

---

## 🧠 How It Works

- The maze is represented as a 2D grid stored in memory.
- Each cell represents either:
  - a free space
  - a wall (obstacle)
- The A\* algorithm:
  - uses **Manhattan distance** as the heuristic
  - maintains an open set using a priority queue
  - expands the most promising node at each step
- The algorithm runs step by step, updating the visualization to show progress.

---

## 🎨 Visualization Legend

| Value | Meaning |
|-----|--------|
| 0 | Free cell |
| 1 | Wall |
| 2 | Open set (frontier) |
| 3 | Closed set (visited) |
| 4 | Final path |
| 5 | Start |
| 6 | Goal |

---

## 🛠 Requirements

- Python 3.10+
- numpy
- matplotlib

Install dependencies:
```bash
pip install numpy matplotlib

▶️ How to Run
python maze.py
A Matplotlib window will open and animate:

node exploration

path expansion

final shortest path from start to goal

"""
AINL3001
BSP 2026
Visualisation utilities file to test visualisation.
"""

from visualisation import draw_grid
import matplotlib.pyplot as plt

GRID_SIZE = 5

START = (0, 0)
GOAL = (4, 4)

OBSTACLES = [
    (1, 1),
    (2, 2)
]

plt.figure(figsize=(6, 6))

draw_grid(
    grid_size=GRID_SIZE,
    start=START,
    goal=GOAL,
    current=(2, 3),
    frontier=[(2, 4), (3, 3)],
    explored=[(0, 0), (1, 0), (1, 2)],
    path=[],
    obstacles=OBSTACLES,
    title="Week 2 Visualisation Test"
)

plt.show()
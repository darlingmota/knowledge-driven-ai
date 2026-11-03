"""
AINL3001
BSP 2026
Visualisation Utilities

This module provides simple visualisations for
search algorithms used throughout the module.

Used in:
    Week 2  - BFS / DFS,
    Week 3  - A*,
    Week 4  - Local Search,
    Week 5  - CSP Visualisation,
    Week 10 - Planning.

Colour Scheme

Green       Start State
Red         Goal State
Black       Obstacles
Light Blue  Frontier
Light Grey  Explored States
Gold        Final Path

"""

import matplotlib.pyplot as plt


def draw_grid(
    grid_size,
    start,
    goal,
    current=None,
    frontier=None,
    explored=None,
    path=None,
    obstacles=None,
    title="Grid World"
):
    """
    Draw a grid showing the current state
    of a search process.

    Parameters
    ----------
    grid_size : int

    start : tuple
        Starting state

    goal : tuple
        Goal state

    current : tuple
        Currently explored node

    frontier : list
        Nodes waiting to be explored

    explored : list
        Nodes already explored

    path : list
        Final solution path

    obstacles : list
        Blocked cells

    title : str
        Figure title
    """

    if frontier is None:
        frontier = []

    if explored is None:
        explored = []

    if path is None:
        path = []

    if obstacles is None:
        obstacles = []

    plt.clf()

    ax = plt.gca()

    # ---------------------------------------
    # Draw cells
    # ---------------------------------------

    for y in range(grid_size):

        for x in range(grid_size):

            state = (x, y)

            colour = "white"

            # explored nodes
            if state in explored:
                colour = "lightgrey"

            # frontier nodes
            if state in frontier:
                colour = "lightskyblue"

            # final path
            if state in path:
                colour = "gold"

            # obstacles
            if state in obstacles:
                colour = "black"

            # start
            if state == start:
                colour = "lightgreen"

            # goal
            if state == goal:
                colour = "lightcoral"

            square = plt.Rectangle(
                (x, y),
                1,
                1,
                facecolor=colour,
                edgecolor="black"
            )

            ax.add_patch(square)

    # ---------------------------------------
    # Current node label
    # ---------------------------------------

    if current is not None:

        plt.text(
            current[0] + 0.5,
            current[1] + 0.5,
            "X",
            ha="center",
            va="center",
            fontsize=12,
            fontweight="bold"
        )

    # ---------------------------------------
    # Axes formatting
    # ---------------------------------------

    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)

    ax.set_xticks(range(grid_size))
    ax.set_yticks(range(grid_size))

    ax.invert_yaxis()

    ax.set_title(title)

    # Nice window title
    try:
        plt.gcf().canvas.manager.set_window_title(
            "AINL3001 Search Visualisation"
        )
    except:
        pass

    plt.pause(0.25)


def show_final_path(
    grid_size,
    start,
    goal,
    path,
    obstacles=None
):
    """
    Display the final path returned
    by a search algorithm.
    """

    if obstacles is None:
        obstacles = []

    plt.figure(figsize=(6, 6))
    plt.clf()

    draw_grid(
        grid_size=grid_size,
        start=start,
        goal=goal,
        path=path,
        obstacles=obstacles,
        title=f"Final Path (Length = {len(path)})"
    )

    plt.show()


def display_legend():
    """
    Prints colour meanings to terminal.
    """

    print("\nVISUALISATION LEGEND")
    print("--------------------")
    print("Green       = Start State")
    print("Red         = Goal State")
    print("Black       = Obstacle")
    print("Light Blue  = Frontier")
    print("Light Grey  = Explored")
    print("Gold        = Final Path")
    print()
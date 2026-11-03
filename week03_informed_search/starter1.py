"""
AINL3001
BSP 2026

Topic 3 Lab

Informed Search and Heuristics

This week we introduce:

0. Manual exploration of heuristics,
1. Manhattan Distance,
2. Greedy Best-First Search,
3. A* Search.

The goal is to compare these algorithms
against BFS from Week 2.

TASKS

Task 0:
    Explore a manual heuristic.
    
Task 1:
    Implement the Manhattan Distance heuristic

Task 2:
    Implement Greedy Best-First Search

Task 3:
    Implement A* Search

Task 4:
    Compare A* against BFS
"""

from collections import deque
import heapq


# --------------------------------------------------
# GRID CONFIGURATION
# --------------------------------------------------

GRID_SIZE = 10

START_STATE = (0, 0)

GOAL_STATE = (9, 9)

OBSTACLES = [
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (5, 6),
    (6, 6),
    (7, 6)
]


# --------------------------------------------------
# HELPER FUNCTIONS
# --------------------------------------------------

def get_neighbours(state):

    x, y = state

    possible_moves = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1)
    ]

    neighbours = []

    for move in possible_moves:

        mx, my = move

        inside_grid = (
            0 <= mx < GRID_SIZE and
            0 <= my < GRID_SIZE
        )

        if inside_grid and move not in OBSTACLES:
            neighbours.append(move)

    return neighbours




import heapq  # pops the smallest item first

# -------*----------------------------------*-------
# TASK 0 - MANUAL HEURISTIC EXPLORATION
# -------------------*------------------------------
# goal is (4, 4)
# A (0, 0) -> 4 + 4 = 8
# B (2, 2) -> 2 + 2 = 4
# C (4, 3) -> 0 + 1 = 1, so C looks closest



# --------------------------------------------------
# TASK 1 - MANHATTAN DISTANCE
# --------------------------------------------------

def manhattan_distance(state, goal):
    """
    Returns Manhattan Distance

    Formula:

    abs(goal_x - current_x)
    +
    abs(goal_y - current_y)
    """

    x, y = state
    goal_x, goal_y = goal
    # steps across plus steps down, ignoring walls
    return abs(goal_x - x) + abs(goal_y - y)


# --------------------------------------------------
# PROVIDED FROM WEEK 2
# --------------------------------------------------

def reconstruct_path(parents, goal):

    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parents[current]

    return list(reversed(path))


# --------------------------------------------------
# TASK 2 - GBFS
# --------------------------------------------------

def greedy_best_first_search(start, goal):

    """
    Implement Greedy Best-First Search

    Only use:

    h(n)

    Ignore:

    path cost so far
    """

    # frontier items are (h, order, state), order breaks ties
    order = 0
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(start, goal), order, start))
    # parents remembers where we came from (and what we've seen)
    parents = {start: None}

    while len(frontier) > 0:
        # take the state that looks closest to the goal
        h, o, current = heapq.heappop(frontier)

        # check if we reached the goal
        if current == goal:
            return reconstruct_path(parents, goal)

        # add new neighbours, ranked only by h
        for neighbour in get_neighbours(current):
            if neighbour not in parents:
                parents[neighbour] = current
                order = order + 1
                h = manhattan_distance(neighbour, goal)
                heapq.heappush(frontier, (h, order, neighbour))

    # no path found
    return None


# --------------------------------------------------
# TASK 3 - ASTAR
# --------------------------------------------------

def astar(start, goal):

    """
    Implement A* Search

    Use:

    f(n) = g(n) + h(n)

    where:

    g(n) = path cost so far

    h(n) = Manhattan Distance
    """

    # frontier items are (f, order, state), order breaks ties
    order = 0
    frontier = []
    heapq.heappush(frontier, (manhattan_distance(start, goal), order, start))
    parents = {start: None}
    # g = cheapest number of steps found so far to each state
    g = {start: 0}

    while len(frontier) > 0:
        # take the state with the lowest f = g + h
        f, o, current = heapq.heappop(frontier)

        # check if we reached the goal
        if current == goal:
            return reconstruct_path(parents, goal)

        for neighbour in get_neighbours(current):
            # each move costs 1
            new_g = g[current] + 1
            # only keep it if it's new or a cheaper way there
            if neighbour not in g or new_g < g[neighbour]:
                g[neighbour] = new_g
                parents[neighbour] = current
                order = order + 1
                f = new_g + manhattan_distance(neighbour, goal)
                heapq.heappush(frontier, (f, order, neighbour))

    # no path found
    return None


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":

    print("Week 3: informed search")
    
    print("TASK 0 - MANUAL HEURISTIC EXPLORATION")
    print("\nConsider the following:")

    print("Goal State =", (4, 4))

    print("\nState A =", (0, 0))

    print("State B =", (2, 2))

    print("State C =", (4, 3))

    print("\nManhattan Distance Example")

    print(
        manhattan_distance(
            (2, 2),
            GOAL_STATE
        )
    )

    print("\nGreedy Search")

    greedy_path = greedy_best_first_search(
        START_STATE,
        GOAL_STATE
    )

    print(greedy_path)

    print("\nA* Search")

    astar_path = astar(
        START_STATE,
        GOAL_STATE
    )

    print(astar_path)
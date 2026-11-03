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




import heapq  # priority queue: always pops the smallest value first

# -------*----------------------------------*-------
# TASK 0 - MANUAL HEURISTIC EXPLORATION
# -------------------*------------------------------
# With goal (4, 4):
#   A (0, 0) -> 4 + 4 = 8 steps away (as the crow walks the grid)
#   B (2, 2) -> 2 + 2 = 4
#   C (4, 3) -> 0 + 1 = 1   <- looks most promising
# A heuristic is just a cheap guess like this that steers the search.



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

    # Manhattan distance = how many grid steps you'd need if there were
    # no walls. It never OVERestimates the true cost (walls only make
    # the trip longer), which is exactly why A* can trust it.
    (x, y), (gx, gy) = state, goal
    return abs(gx - x) + abs(gy - y)


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

    # Greedy always expands whichever frontier state LOOKS closest to the
    # goal (smallest h). It's fast, but it ignores how far it has already
    # walked, so it can be lured into a longer route.
    counter = 0                      # tie-breaker so heapq never compares tuples of states
    frontier = [(manhattan_distance(start, goal), counter, start)]
    parents = {start: None}

    while frontier:
        _, _, state = heapq.heappop(frontier)
        if state == goal:
            return reconstruct_path(parents, goal)

        for nxt in get_neighbours(state):
            if nxt not in parents:   # parents doubles as our visited set
                parents[nxt] = state
                counter += 1
                heapq.heappush(frontier, (manhattan_distance(nxt, goal), counter, nxt))

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

    # A* ranks states by f = g + h:
    #   g = steps actually taken to get here
    #   h = Manhattan guess of steps still to go
    # With a heuristic that never overestimates, the first time we POP the
    # goal we have the cheapest path.
    counter = 0
    frontier = [(manhattan_distance(start, goal), counter, start)]
    parents = {start: None}
    g_cost = {start: 0}              # best known cost to reach each state

    while frontier:
        _, _, state = heapq.heappop(frontier)
        if state == goal:
            return reconstruct_path(parents, goal)

        for nxt in get_neighbours(state):
            new_g = g_cost[state] + 1          # every move costs 1
            # Only (re)queue a state if we found a cheaper way to reach it.
            if nxt not in g_cost or new_g < g_cost[nxt]:
                g_cost[nxt] = new_g
                parents[nxt] = state
                counter += 1
                f = new_g + manhattan_distance(nxt, goal)
                heapq.heappush(frontier, (f, counter, nxt))

    return None


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":

    print("=" * 50)
    print("WEEK 3")
    print("=" * 50)
    
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
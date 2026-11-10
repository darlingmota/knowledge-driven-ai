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
# C (4, 3) -> 0 + 1 = 1, so C looks closest and A looks furthest
# that's useful because it tells the search what to try first
# it is not the actual path though, and manhattan doesn't know about walls



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

# greedy always expands the lowest h, so it aims at the goal
# bfs ignores the goal and goes level by level, so its first hit is a shortest path
# greedy is not always shortest. if h leads it into a wall it can take a long detour


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

# g is the cost so far, h is the estimated cost left, f = g + h is the estimated total
# a* uses f, greedy uses only h, bfs uses neither


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

    # both greedy and a* found the same 18 move path (19 states), along the top then down the right
    # that's optimal because manhattan from start to goal is 18
    # the printed manhattan example is 14 because it uses GOAL_STATE (9, 9), not the task 1 goal (4, 4)
    # this file doesn't run bfs or print node counts. on this grid greedy expanded 19 states
    # and generated 34, while a* and bfs both expanded all 93 free cells and also found an 18 move path
    # a* still has h, but a lot of cells have the same f value as 18 so it doesn't skip much here

    # uninformed search (bfs/dfs) has no estimate of distance to the goal. informed search uses a heuristic
    # a* is informed because of h. bfs doesn't need one because it already explores systematically
    # a heuristic is an estimate of the cost left. that's h(n). g(n) is the cost so far. f is g+h
    # greedy uses only h, a* uses g+h so it won't forget about the path already taken
    # a useful heuristic is cheap, close to the true cost, and ideally never overestimates if you want a* to stay optimal
    # obstacles don't change the heuristic, but they can make a low h misleading if a wall is in the way
    # i didn't put h=0 in this file. if h is always 0 then f is just g, so a* acts like uniform-cost (like bfs here)
    # i tried that on this same grid and it also expanded 93 and still found the 18 move path
    # reused from week 2: neighbours, parents, and reconstruct_path. only the frontier ranking is new
    # if every problem and search stay tightly mixed, you end up rewriting the same search for every new problem

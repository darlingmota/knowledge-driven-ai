"""
AINL3001 - Knowledge-Driven AI
BSP 2026
Topic 2: Uninformed Search

In Week 1 we represented a problem as states and actions.

This week we will explore a state space using:

1. Breadth-First Search (BFS),
2. Depth-First Search (DFS).

----------------------------------------------------
YOUR TASKS

Task 1:
    Complete the BFS algorithm

Task 2:
    Complete the DFS algorithm

Task 3:
    Compare the paths returned

Task 4:
    Explain the differences between BFS and DFS

----------------------------------------------------
"""

# the collections functionality is not used yet in the 
# starter.py. It is your job to make use of it for the
# solution.
from collections import deque


# --------------------------------------------------
# GRID CONFIGURATION
# --------------------------------------------------

GRID_SIZE = 5

START_STATE = (0, 0)

GOAL_STATE = (4, 4)

OBSTACLES = [
    (1, 1),
    (2, 2),
    (3, 2)
]


# --------------------------------------------------
# HELPER FUNCTION
# --------------------------------------------------

def get_neighbours(state):
    """
    Returns all valid neighbouring states.

    A valid move:
        - stays inside the grid
        - does not move into an obstacle
    """

    x, y = state

    possible_moves = [
        (x + 1, y),  # right
        (x - 1, y),  # left
        (x, y + 1),  # down
        (x, y - 1)   # up
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


# --------------------------------------------------
# TASK 1 - BFS
# --------------------------------------------------

def bfs(start, goal):
    """
    Breadth-First Search

    TODO:

    1. Create a queue,
    2. Create a visited set,
    3. Explore states,
    4. Return path when goal is found.

    Hint:
        Use deque()
    """

    # remove pass for your solution. This is only here to 
    # make sure that there are no errors displayed.
    # BFS explores the grid in "rings": everything 1 step away, then 2 steps...
    # A queue (first in, first out) gives us exactly that order.
    # Each queue entry is a whole path, so when we reach the goal
    # the route is already built for us.
    queue = deque([[start]])
    visited = {start}  # mark states when we ADD them, so nothing is queued twice

    while queue:
        path = queue.popleft()      # oldest path first
        state = path[-1]            # where that path currently ends

        if state == goal:
            return path             # first time we reach the goal = shortest path

        for nxt in get_neighbours(state):
            if nxt not in visited:
                visited.add(nxt)
                queue.append(path + [nxt])

    return None  # queue ran dry: the goal can't be reached


# --------------------------------------------------
# TASK 2 - DFS
# --------------------------------------------------

def dfs(start, goal):
    """
    Depth-First Search

    TODO:

    1. Create a stack,
    2. Create a visited set,
    3. Explore states,
    4. Return path when goal is found.

    Hint:
        A Python list can be used as a stack
    """
    
    # remove pass for your solution. This is only here to 
    # make sure that there are no errors displayed.
    # DFS dives as deep as it can down one route before backing up.
    # A plain list used as a stack (last in, first out) does that.
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()          # newest path first
        state = path[-1]

        if state in visited:
            continue                # already explored from here
        visited.add(state)

        if state == goal:
            return path             # a valid path, but not necessarily the shortest

        for nxt in get_neighbours(state):
            if nxt not in visited:
                stack.append(path + [nxt])

    return None


# --------------------------------------------------
# DEMONSTRATION SECTION
# --------------------------------------------------

print("===================================")
print(" WEEK 2 - UNINFORMED SEARCH")
print("===================================")

print("\nStart State:")
print(START_STATE)

print("\nGoal State:")
print(GOAL_STATE)

print("\nObstacles:")
print(OBSTACLES)

print("\nNeighbours of Start State:")
print(get_neighbours(START_STATE))

print("\nRunning BFS...")
bfs_path = bfs(START_STATE, GOAL_STATE)

print("BFS Path:")
print(bfs_path)

print("\nRunning DFS...")
dfs_path = dfs(START_STATE, GOAL_STATE)

print("DFS Path:")
print(dfs_path)


# --------------------------------------------------
# REFLECTION QUESTIONS
# --------------------------------------------------

"""
Be prepared to discuss:

1. What data structure does BFS use?

2. What data structure does DFS use?

3. Why does BFS usually return a shorter path?

4. Which algorithm explores more states?

5. What effect do obstacles have?

"""

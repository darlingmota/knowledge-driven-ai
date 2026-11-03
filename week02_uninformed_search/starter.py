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
    # queue holds paths, start with just the start state
    queue = deque()
    queue.append([start])
    visited = set()
    visited.add(start)

    while len(queue) > 0:
        # take the oldest path out of the queue
        path = queue.popleft()
        current = path[-1]

        # check if we reached the goal
        if current == goal:
            return path

        # add each new neighbour to the end of the queue
        for neighbour in get_neighbours(current):
            if neighbour not in visited:
                visited.add(neighbour)
                new_path = path + [neighbour]
                queue.append(new_path)

    # no path found
    return None


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
    # stack holds paths, start with just the start state
    stack = []
    stack.append([start])
    visited = set()

    while len(stack) > 0:
        # take the newest path off the stack
        path = stack.pop()
        current = path[-1]

        # skip it if we've been here already
        if current in visited:
            continue
        visited.add(current)

        # check if we reached the goal
        if current == goal:
            return path

        # push each new neighbour onto the stack
        for neighbour in get_neighbours(current):
            if neighbour not in visited:
                new_path = path + [neighbour]
                stack.append(new_path)

    # no path found
    return None


# --------------------------------------------------
# DEMONSTRATION SECTION
# --------------------------------------------------

print("Week 2: uninformed search")

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

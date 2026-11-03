"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Topic 1 Lab: Representing Problems

--------------------------------------------------
PURPOSE OF THIS LAB

In AI, before we solve a problem, we must DEFINE IT.

This week, we are NOT writing search algorithms.
Instead, we are learning how to represent a problem
in a way that a computer can understand.

The key idea is that AI works by exploring 
a so called "state space".

--------------------------------------------------
CORE CONCEPTS

State:
    A representation of "where we are".
    Example: (x, y) position in a grid

Actions:
    What we can do from a state.
    Example: move up, down, left, right

Transition:
    What happens when we take an action.

--------------------------------------------------
YOUR TASKS

You will:
1. Represent a grid world.
2. Define a function that returns valid moves.
3. Explore the state space.

"""

# --------------------------------------------------
# STEP 1: Define the grid size
# --------------------------------------------------

GRID_SIZE = 5  # This creates a 5x5 grid


# --------------------------------------------------
# STEP 2: Define a STATE
# --------------------------------------------------

# A state will be represented as a tuple (x, y)
# Example: (0, 0) is top-left
start_state = (0, 0)


# --------------------------------------------------
# TASK 1: Neighbour Function
# --------------------------------------------------
# This function should return all valid moves from a state

def get_neighbours(state):
    """
    Given a state (x, y), return all valid neighbouring states.

    TODO:
    - Allow movement:
        up    -> (x, y-1)
        down  -> (x, y+1)
        left  -> (x-1, y)
        right -> (x+1, y)

    - BUT: Do not allow moves outside the grid

    Example:
        Input: (0,0)
        Output should NOT include negative coordinates

    """
    
    # TODO: Replace this with your own code
    neighbours = []

    x, y = state

    # The four moves, written as (dx, dy) changes to the position.
    # Remember y grows DOWNWARDS here, so "up" means y - 1.
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        # Only keep the move if it stays on the board.
        # Valid coordinates run from 0 to GRID_SIZE - 1 in both directions.
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            neighbours.append((nx, ny))

    # Corners get 2 neighbours, edges get 3, the middle gets 4.

    return neighbours


# --------------------------------------------------
# TASK 2: Test your function
# --------------------------------------------------

print("Testing neighbours function...")
print("Start state:", start_state)

neighbours = get_neighbours(start_state)

print("Neighbours:", neighbours)


# --------------------------------------------------
# TASK 3: Try different states
# --------------------------------------------------

test_states = [
    (0, 0),   # corner
    (2, 2),   # middle
    (4, 4),   # opposite corner
]

print("\nTesting multiple states:")

for s in test_states:
    print(f"State {s} -> {get_neighbours(s)}")


# --------------------------------------------------
# EXTENSION TASKS (Optional)
# --------------------------------------------------

"""
Try extending your solution:

1. Add obstacles:
   - Define blocked cells
   - Prevent moving into them

2. Visualise the grid:
   - Print the grid and mark current position

3. Count number of neighbours for each state

--------------------------------------------------
REFLECTION QUESTIONS (Be ready to answer)

- What exactly is a "state" in this problem?
- What makes a move valid or invalid?
- Why is defining the problem important BEFORE solving it?

--------------------------------------------------
DEMO EXPECTATION

You should be able to:
- Explain your code,
- Show correct neighbours,
- Discuss edge cases (corners, boundaries).

"""
"""
AINL3001 — Knowledge-Driven AI
Week 4 — Local Search and Optimisation
BSP 2026

This week introduces local search.

In previous weeks, search algorithms explored paths through
a state space in order to reach a goal.

Local search takes a different approach:

    1. Start with a state.
    2. Evaluate how good that state is.
    3. Generate neighbouring states.
    4. Move to a better neighbour.
    5. Repeat.

We will explore this using the N-Queens problem.

Tasks
-----

1. Understand the problem representation.
2. Implement conflict counting.
3. Explore neighbouring states.
4. Implement Hill Climbing.
5. Implement Simulated Annealing.
"""

import math
import random

from queens_problem import QueensProblem

N = 8


# --------------------------------------------------
# TASK 0 — UNDERSTANDING THE STATE
# --------------------------------------------------

example_board = [0, 1, 2, 3]

print("Manual Exploration Board:")
print(example_board)

print(
    "\nEach list position represents a column."
)

print(
    "Each value represents the row containing the queen."
)

print(
    "\nQuestion: How many conflicts exist on this board?"
)


# --------------------------------------------------
# TASK 1 — EVALUATE A STATE
# --------------------------------------------------

def count_conflicts(board):
    """
    Return the number of pairs of queens
    that attack each other.

    Lower values are better.

    A solution has:

        conflict count = 0
    """

    # TODO:
    # Compare each queen with every queen
    # that comes after it.
    #
    # Queens conflict when they are:
    #
    #   1. in the same row
    #   2. on the same diagonal

    conflicts = 0
    # compare each pair of queens once
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            # same row
            if board[i] == board[j]:
                conflicts = conflicts + 1
            # same diagonal: row gap equals column gap
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts = conflicts + 1
    return conflicts


# --------------------------------------------------
# TASK 2 — EXPLORE THE PROBLEM
# --------------------------------------------------

def generate_neighbours(problem, board):
    """
    Generate all neighbouring boards.

    Use the Problem interface introduced this week:

        problem.actions(state)
        problem.result(state, action)
    """

    neighbours = []

    # TODO:
    #
    # 1. Ask the problem for the available actions.
    # 2. Apply each action.
    # 3. Add the resulting state to neighbours.
    # apply every action to get every neighbour
    for action in problem.actions(board):
        new_board = problem.result(board, action)
        neighbours.append(new_board)

    return neighbours


# --------------------------------------------------
# TASK 3 — HILL CLIMBING
# --------------------------------------------------

def hill_climbing(problem, start_board):
    """
    Use Hill Climbing to reduce the number
    of conflicts.

    Algorithm:

        current = start state

        repeat:

            generate neighbours

            find the neighbour with the
            lowest conflict count

            if the neighbour is not better:
                stop

            otherwise:
                move to the neighbour

        return current
    """

    current = start_board

    current_cost = count_conflicts(current)
    steps = 0

    while True:
        # find the neighbour with the fewest conflicts
        best = None
        best_cost = None
        for neighbour in generate_neighbours(problem, current):
            cost = count_conflicts(neighbour)
            if best is None or cost < best_cost:
                best = neighbour
                best_cost = cost

        # stop if it's not better than where we are
        if best_cost >= current_cost:
            break

        # move to the better neighbour
        current = best
        current_cost = best_cost
        steps = steps + 1

    print(f"Hill Climbing stopped after {steps} steps with {current_cost} conflicts")
    return current


# --------------------------------------------------
# TASK 4 — SIMULATED ANNEALING
# --------------------------------------------------

def simulated_annealing(problem, start_board):
    """
    Use Simulated Annealing to search for
    a solution.

    Unlike Hill Climbing, Simulated Annealing
    can sometimes accept a worse state.

    This can help escape local minima.
    """

    current = start_board

    temperature = 10.0
    cooling_rate = 0.95

    current_cost = count_conflicts(current)
    steps = 0

    # keep going until solved or it's basically cold
    while current_cost > 0 and temperature > 0.001:
        # pick one random neighbour
        action = random.choice(problem.actions(current))
        candidate = problem.result(current, action)
        candidate_cost = count_conflicts(candidate)

        # negative change means it's better
        change = candidate_cost - current_cost

        # always take better moves
        if change < 0:
            current = candidate
            current_cost = candidate_cost
        # sometimes take worse moves, less often as it cools
        elif random.random() < math.exp(-change / temperature):
            current = candidate
            current_cost = candidate_cost

        # cool down a bit
        temperature = temperature * cooling_rate
        steps = steps + 1

    print(f"Simulated Annealing stopped after {steps} steps with {current_cost} conflicts")
    return current


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":

    board = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    problem = QueensProblem(board)

    print("\nRandom Board")
    print(board)

    print("\nConflicts")
    print(
        count_conflicts(board)
    )

    print("\nPossible Actions")

    actions = problem.actions(board)

    print(
        f"{len(actions)} actions available"
    )

    print("\nNeighbours")

    neighbours = generate_neighbours(
        problem,
        board
    )

    print(
        f"{len(neighbours)} neighbours generated"
    )
    # task 0: all 4 queens are on one diagonal, so all 6 pairs clash
    print("\nConflicts on the manual board:", count_conflicts(example_board))

    print("\nHill Climbing")
    hc_board = hill_climbing(problem, board)
    print(hc_board, "->", count_conflicts(hc_board), "conflicts")

    print("\nSimulated Annealing")
    sa_board = simulated_annealing(problem, board)
    print(sa_board, "->", count_conflicts(sa_board), "conflicts")

    # try both on lots of random boards and count the solves
    import contextlib, io
    trials = 50
    hc_wins = 0
    sa_wins = 0
    for t in range(trials):
        b = [random.randint(0, N - 1) for _ in range(N)]
        # hide the prints from each run
        with contextlib.redirect_stdout(io.StringIO()):
            if count_conflicts(hill_climbing(problem, b)) == 0:
                hc_wins = hc_wins + 1
            if count_conflicts(simulated_annealing(problem, b)) == 0:
                sa_wins = sa_wins + 1
    print(f"\nOut of {trials} random boards: Hill Climbing solved {hc_wins}, "
          f"Simulated Annealing solved {sa_wins}")

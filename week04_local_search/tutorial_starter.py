"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

In previous weeks, we represented problems directly using
variables and functions.

From this week onwards, we will use a common Problem class
where appropriate.

This tutorial uses the familiar grid world from earlier weeks
to explore the new structure.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT

        Remember: an action must not move outside the grid.
        """

        x, y = state
        actions = []
        # only add a direction if it stays on the grid
        if y > 0:
            actions.append("UP")
        if y < GRID_SIZE - 1:
            actions.append("DOWN")
        if x > 0:
            actions.append("LEFT")
        if x < GRID_SIZE - 1:
            actions.append("RIGHT")
        return actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """

        x, y = state
        # move one square in the chosen direction
        if action == "UP":
            return (x, y - 1)
        if action == "DOWN":
            return (x, y + 1)
        if action == "LEFT":
            return (x - 1, y)
        if action == "RIGHT":
            return (x + 1, y)


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

if actions is not None:
    for action in actions:

        new_state = problem.result(
            (0, 0),
            action
        )

        print(
            action,
            "->",
            new_state
        )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)


# reflection
# problem.initial is the starting state, here (0, 0)
# problem.goal is the target, here (4, 4)
# actions(state) lists the moves you can make from here. result(state, action) applies one move and returns the new state
# Problem is just a general template, so it doesn't know about grids and can be reused for other tasks
# GridProblem only describes the world. the search stays separate, which is why the same structure also works for 8-queens
# yes, anything with states and actions can use it, like n-queens

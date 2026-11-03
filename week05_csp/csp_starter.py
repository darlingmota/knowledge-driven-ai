"""
AINL3001 — Knowledge-Driven AI
Week 5 — Constraint Satisfaction Problems
BSP 2026

Australian map colouring: six regions and three colours.

Tasks
-----
0. Examine an invalid assignment.
1. Understand variables, domains and constraints.
2. Implement constraint checking.
3. Implement backtracking with simple variable selection.
4. Compare backtracking with brute force.
5. Improve variable selection using MRV.

Work in this starter file and commit your progress to your own fork.
"""

# --------------------------------------------------
# TASK 0 — MANUAL EXPLORATION
# --------------------------------------------------

example_assignment = {
    "WA": "Red",
    "NT": "Red",
    "SA": "Green",
    "Q": "Blue",
    "NSW": "Red",
    "V": "Green",
}

print("Manual CSP Exploration")
print(example_assignment)
print("\nQuestions:")
print("1. Is this assignment valid?")
print("2. Which neighbouring pairs violate a constraint?")
print("3. How could you correct the assignment?")
print("4. Why is it useful to detect violations early?")

# --------------------------------------------------
# TASK 1 — CSP REPRESENTATION
# --------------------------------------------------

# Each variable is an Australian region.
variables = ["WA", "NT", "SA", "Q", "NSW", "V"]

# Each region may use one of these three colours.
domains = {
    variable: ["Red", "Green", "Blue"]
    for variable in variables
}

# Each pair of neighbouring regions must have different colours.
constraints = [
    ("WA", "NT"),
    ("WA", "SA"),
    ("NT", "SA"),
    ("NT", "Q"),
    ("SA", "Q"),
    ("SA", "NSW"),
    ("SA", "V"),
    ("Q", "NSW"),
    ("NSW", "V"),
]

# --------------------------------------------------
# TASK 2 — CONSTRAINT CHECKING
# --------------------------------------------------

def is_valid_assignment(assignment):
    """Return True if a complete OR partial assignment is valid."""
    # TODO:
    # 1. Loop over neighbouring pairs in constraints.
    # 2. If BOTH regions have been assigned, compare their colours.
    # 3. Return False if neighbouring regions have the same colour.
    # 4. Otherwise return True.
    for a, b in constraints:
        # A pair only matters once BOTH sides have a colour. That's what
        # lets us reject bad partial assignments early.
        if a in assignment and b in assignment and assignment[a] == assignment[b]:
            return False
    return True


# --------------------------------------------------
# TASK 3 AND TASK 5 — VARIABLE SELECTION
# --------------------------------------------------

def select_unassigned_variable(assignment):
    """Choose the next unassigned region.

    Task 3: First return the FIRST unassigned region.

    Task 5: Replace that approach with MRV (Minimum Remaining Values):
    choose the unassigned region with the FEWEST currently legal
    colours. Break ties by keeping the first region in variables.
    """
    # TASK 3 TODO:
    # Return the first variable not in assignment, or None if all
    # variables have been assigned.
    #
    # TASK 5 TODO (after backtracking works):
    # For each unassigned variable, temporarily try each colour,
    # check is_valid_assignment(), and undo the temporary assignment.
    # Count legal colours and choose the variable with the fewest.
    unassigned = [v for v in variables if v not in assignment]
    if not unassigned:
        return None

    # Task 3 version was simply: return unassigned[0]
    #
    # Task 5, MRV: pick the region with the fewest colours still allowed.
    # The most "boxed-in" region is the one most likely to fail, so we
    # tackle it first and find dead ends sooner ("fail first").
    def legal_colour_count(var):
        count = 0
        for colour in domains[var]:
            assignment[var] = colour          # try it...
            if is_valid_assignment(assignment):
                count += 1
            del assignment[var]               # ...and undo it straight away
        return count

    # min() keeps the first one on ties, so ties follow the order in variables.
    return min(unassigned, key=legal_colour_count)


nodes_explored = 0  # counts colour attempts, for comparing with brute force

# --------------------------------------------------
# TASK 3 — BACKTRACKING SEARCH
# --------------------------------------------------

def backtracking_search(assignment):
    """Return a complete valid assignment, or None if none exists."""
    # TODO:
    # 1. If every variable has been assigned, return a COPY.
    # 2. Choose a variable with select_unassigned_variable().
    # 3. For each colour in its domain, temporarily assign it.
    # 4. If the partial assignment is valid, search recursively.
    # 5. Return the recursive result if a solution was found.
    # 6. Otherwise remove the temporary assignment (backtrack).
    # 7. Return None if every colour fails.
    global nodes_explored
    if len(assignment) == len(variables):
        return dict(assignment)               # copy, so later undos can't change it

    var = select_unassigned_variable(assignment)
    for colour in domains[var]:
        assignment[var] = colour
        nodes_explored += 1
        # Only go deeper if nothing is broken yet. A bad partial
        # assignment gets cut off here, along with every completion of it.
        if is_valid_assignment(assignment):
            result = backtracking_search(assignment)
            if result is not None:
                return result
        del assignment[var]                   # backtrack: undo and try the next colour
    return None                               # every colour failed -> tell the caller


# --------------------------------------------------
# TASK 4 — BRUTE FORCE COMPARISON
# --------------------------------------------------

# Six regions with three possible colours each give 3 ** 6 = 729
# complete assignments. Why can backtracking avoid checking all 729?
#
# Answer: it checks constraints on PARTIAL assignments. As soon as two
# neighbours clash, every one of the completions below that point is
# skipped in one go. Brute force would build and test each one.
#
# Task 0 answers: the example is NOT valid. Two pairs clash:
#   WA-NT (both Red) and SA-V (both Green).
# One fix: WA -> Blue (its neighbours are NT=Red, SA=Green) and
# V -> Blue (its neighbours are SA=Green, NSW=Red).


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("WEEK 5 — CONSTRAINT SATISFACTION PROBLEMS")
    print("=" * 50)

    print("\nVariables:", variables)
    print("Domains:", domains)
    print("Constraints:", constraints)

    print("\nExample assignment valid?")
    print(is_valid_assignment(example_assignment))  # Expected: False

    partial_assignment = {"WA": "Red", "NT": "Green"}
    print("\nPartial assignment valid?")
    print(is_valid_assignment(partial_assignment))  # Expected: True

    print("\nSearching for a solution...")
    solution = backtracking_search({})
    print("Solution:", solution)

    if solution is not None:
        print("\nSolution valid?", is_valid_assignment(solution))
        print("\nColour assignment:")
        for region in variables:
            print(f"{region:4} -> {solution[region]}")
    else:
        print("No solution yet. Complete the TODO sections.")

    print("Colour attempts made by backtracking:", nodes_explored)
    print("\nPossible complete assignments:", 3 ** len(variables))
    print("\nReflection:")
    print("1. What causes backtracking?")
    print("2. Why can backtracking be faster than brute force?")
    print("3. Why might MRV reduce search?")
    print("4. How could this model represent timetabling?")
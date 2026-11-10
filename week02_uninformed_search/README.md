# Week 2 — Uninformed Search

**TU850-3 — AINL3001 Knowledge-Driven AI**  
**Dr. Bianca Schoen-Phelan**  
**2026**

## Learning Objectives

By the end of this lab, you should be able to:

- Implement Breadth-First Search (BFS) and Depth-First Search (DFS).
- Understand the differences between search strategies.
- Use a queue for BFS and a stack for DFS.
- Track visited states during search.
- Apply search algorithms to the grid world introduced in Week 1.
- Recognise limitations of unstructured search code.

## Context

Search algorithms explore a **state space** to find a solution path from an initial state to a goal state.

In Week 1, we represented a problem using states, actions, and a simple grid world.

This week, we will use the same grid-world idea to explore two **uninformed search algorithms**:

- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

They are called *uninformed* because they do not use additional information about how close a state is to the goal.

Both algorithms explore the same state space, but they differ in **which state they choose to explore next**.

## Starter Code

Open:

```text
week02_uninformed_search/starter.py
```

The starter code contains the grid configuration:

```python
GRID_SIZE = 5

START_STATE = (0, 0)

GOAL_STATE = (4, 4)

OBSTACLES = [
    (1, 1),
    (2, 2),
    (3, 2)
]
```

A state is represented as an `(x, y)` coordinate.

For example:

```python
(0, 0)
```

represents the start state.

The function:

```python
get_neighbours(state)
```

returns the valid neighbouring states that can be reached from a given state.

A valid move must:

- Stay inside the grid.
- Avoid obstacles.

Before implementing the search algorithms, read through `get_neighbours()` and make sure you understand what it does.

## Task 1 — Implement BFS

Complete:

```python
def bfs(start, goal):
```

Breadth-First Search explores states **level by level**.

BFS uses a **queue**.

The starter code already imports:

```python
from collections import deque
```

Use `deque` to implement your queue.

Your BFS implementation should:

1. Create a queue.
2. Add the starting state.
3. Create a set to track visited states.
4. Explore states from the queue.
5. Generate neighbouring states using `get_neighbours()`.
6. Avoid repeatedly exploring states that have already been visited.
7. Return the path when the goal is found.

### Think About

If you store only the current state in the queue, how will you know the path that was taken to reach it?

You may find it useful to store both:

```text
(state, path)
```

in the queue.

## Task 2 — Implement DFS

Complete:

```python
def dfs(start, goal):
```

Depth-First Search explores one branch of the state space before returning to explore alternatives.

DFS can be implemented using recursion or a **stack**.

For this lab, you can use a Python list as a stack.

For example:

```python
stack.append(item)
```

adds an item to the stack, while:

```python
stack.pop()
```

removes the most recently added item.

Your DFS implementation should:

1. Create a stack.
2. Add the starting state.
3. Create a set to track visited states.
4. Explore states from the stack.
5. Generate neighbouring states using `get_neighbours()`.
6. Avoid repeatedly exploring states that have already been visited.
7. Return the path when the goal is found.

## Task 3 — Apply BFS and DFS to the Grid

Run both algorithms using:

```python
START_STATE
```

and:

```python
GOAL_STATE
```

The demonstration section in `starter.py` runs:

```python
bfs_path = bfs(START_STATE, GOAL_STATE)
```

and:

```python
dfs_path = dfs(START_STATE, GOAL_STATE)
```

Run your program and examine the paths returned.

Compare the results.

| Algorithm | Path | Path Length |
|---|---|---|
| BFS |  |  |
| DFS |  |  |

Consider:

- Do both algorithms find the goal?
- Do they return the same path?
- Which path is shorter?
- Why are the paths different?

## Task 4 — Compare BFS and DFS

Compare the behaviour of the two search algorithms.

### Breadth-First Search

BFS uses a:

```text
QUEUE
```

A queue follows:

```text
First In, First Out (FIFO)
```

This causes BFS to explore states level by level.

### Depth-First Search

DFS uses a:

```text
STACK
```

A stack follows:

```text
Last In, First Out (LIFO)
```

This causes DFS to explore one branch before returning to explore alternatives.

Think about how this difference affects the paths returned by the algorithms.

## Experiment

Try changing the grid.

For example, change:

```python
START_STATE
```

or:

```python
GOAL_STATE
```

You can also change the obstacle positions:

```python
OBSTACLES = [
    (1, 1),
    (2, 2),
    (3, 2)
]
```

Run BFS and DFS again.

Observe how the paths change.

Consider:

- Does BFS still find a path?
- Does DFS still find a path?
- Do they explore the grid in the same way?
- What happens if obstacles block the route to the goal?

## Reflection Questions

Be prepared to discuss the following questions:

1. What data structure does BFS use?
2. What data structure does DFS use?
3. Which algorithm finds shorter paths in this grid?
4. Why can BFS find a shorter path than DFS?
5. Which algorithm explores more states?
6. What effect do obstacles have on the search?
7. Why do we need to keep track of visited states?
8. Where is code duplicated between the BFS and DFS implementations?
9. What parts of the code describe the **problem**, and what parts implement the **search algorithm**?
10. How might we organise this code differently so that different search algorithms could work with different problems?

## Summary

In this lab, you implemented two uninformed search algorithms:

```text
Breadth-First Search
        ↓
      Queue
        ↓
       FIFO
```

and:

```text
Depth-First Search
        ↓
      Stack
        ↓
       LIFO
```

Both algorithms:

- Begin at an initial state.
- Maintain a frontier of states to explore.
- Track visited states.
- Generate neighbouring states.
- Search for a goal.
- Return a path when the goal is found.

The main difference is the order in which they explore the state space.

You should also have noticed that the current program mixes together:

- The definition of the problem.
- The grid representation.
- The generation of valid moves.
- The search algorithms.

This works for a small example, but as our problems and algorithms become more complex, we will need to think about how this code could be organised more clearly.

In **Week 3**, we will build on BFS and DFS by introducing **informed search**, where additional information is used to guide the search towards the goal.

## My answers

1. BFS uses a queue, so it works FIFO and always expands the oldest path first.
2. DFS uses a stack, so it works LIFO and always expands the newest path first.
3. BFS found the shorter path. On my run it was 8 moves, and DFS was 12.
4. BFS goes level by level, so the first time it reaches the goal it's already found a shortest path. DFS dives down one branch first, so it can find a longer route.
5. On this grid they both ended up visiting all 22 free cells, so neither explored more than the other. The difference was the path length, not how many states they looked at.
6. Obstacles just block those cells, so the path has to go around them. If they completely blocked the way to the goal, neither algorithm would find a path.
7. We keep a visited set so we don't go back to the same cell again and get stuck in a loop.
8. Most of the BFS and DFS code is the same: neighbours, the visited set, building the path, and the goal test. The only real difference is queue vs stack.
9. The grid, start, goal, obstacles and get_neighbours are the problem. bfs and dfs are the search.
10. I'd put the problem in its own class, with the states, actions and goal test, and keep the search algorithms separate so they can be reused on different problems. That's what we did later with the Problem class.

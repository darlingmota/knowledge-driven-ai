# Week 3 — Informed Search

**TU850-3 — AINL3001 Knowledge-Driven AI**  
**Dr. Bianca Schoen-Phelan**  
**2026**

## Learning Objectives

By the end of this lab, you should be able to:

- Explain the difference between **uninformed** and **informed** search.
- Understand the role of a **heuristic**.
- Calculate Manhattan Distance.
- Implement Greedy Best-First Search.
- Implement A* Search.
- Compare BFS and A*.
- Evaluate the quality of a heuristic.
- Explain how a heuristic can affect search behaviour.

> **Assessment:** This lab is a CA exercise worth **2% of your module mark**.

## Background

In Week 2, we explored a state space using:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)

These algorithms are examples of **uninformed search**.

They do not use information about how close a state is to the goal when deciding which state to explore next.

This week, we introduce a new question:

> **Can we guide the search towards the goal?**

The answer is a **heuristic**.

A heuristic is an estimate of how far a state is from the goal.

A useful heuristic can reduce the amount of search required by helping the algorithm decide which states appear more promising.

## Scenario

You are building navigation software for a delivery robot.

The robot must travel across a grid world from a start location to a goal location while avoiding obstacles.

In Week 2, BFS explored the grid without using information about the location of the goal.

This week, the robot is allowed to use information about the destination to help decide which state to explore next.

We will investigate two informed search algorithms:

- **Greedy Best-First Search**
- **A\* Search**

# Part A — Exploring Heuristics

## Manhattan Distance

For a grid where movement is horizontal or vertical, one possible heuristic is **Manhattan Distance**.

The Manhattan Distance between two positions is:

```text
distance = |x₁ - x₂| + |y₁ - y₂|
```

Consider the following goal:

```text
Goal = (4, 4)
```

and three states:

```text
State A = (0, 0)
State B = (2, 2)
State C = (4, 3)
```

## Task 1 — Calculate Manhattan Distance

Calculate the Manhattan Distance from each state to the goal.

Complete the table:

| State | Position | Manhattan Distance to Goal |
|---|---|---:|
| A | `(0, 0)` | |
| B | `(2, 2)` | |
| C | `(4, 3)` | |

### Questions

1. Which state appears closest to the goal?
2. Which state appears furthest from the goal?
3. Why might this information be useful during search?
4. Does the Manhattan Distance tell us the actual path the robot must take?
5. What information might the heuristic not know about?

# Part B — Greedy Best-First Search

Greedy Best-First Search uses the heuristic to decide which state to explore next.

It prefers the state that **appears closest to the goal**.

We can describe this as:

```text
Choose the state with the lowest h(n)
```

where:

```text
h(n) = estimated cost from state n to the goal
```

The basic idea is:

```text
Current Search
      ↓
Generate Neighbours
      ↓
Calculate h(n)
      ↓
Choose State with Lowest h(n)
      ↓
Continue Search
```

Greedy Best-First Search focuses on the estimated distance to the goal.

It does **not** take into account the cost of the path already travelled.

## Task 2 — Implement Greedy Best-First Search

Open the supplied starter code and locate the Greedy Best-First Search function.

Complete the algorithm.

Your implementation should:

1. Begin at the start state.
2. Maintain a frontier of states to explore.
3. Track visited states.
4. Generate valid neighbouring states.
5. Calculate the heuristic value for candidate states.
6. Choose the state with the lowest heuristic value.
7. Continue until the goal is reached.
8. Return the path to the goal.

### Questions

- How does Greedy Best-First Search decide which state to explore next?
- How is this different from BFS?
- Does Greedy Best-First Search always find the shortest path?
- What could happen if the heuristic guides the search towards a poor route?

# Part C — A* Search

Greedy Best-First Search considers how close a state **appears** to be to the goal.

However, it ignores how expensive the path has already been.

A* combines both pieces of information.

A* uses:

```text
f(n) = g(n) + h(n)
```

where:

```text
g(n) = path cost from the start to state n
```

and:

```text
h(n) = heuristic estimate from state n to the goal
```

Therefore:

```text
f(n) = cost so far + estimated cost remaining
```

This gives A* information about both the path already travelled and the estimated distance still to go.

## Task 3 — Implement A* Search

Locate the A* function in the supplied starter code.

Complete the algorithm.

Your implementation should:

1. Begin at the start state.
2. Maintain a frontier.
3. Track the path cost `g(n)`.
4. Calculate the heuristic `h(n)`.
5. Calculate:

```text
f(n) = g(n) + h(n)
```

6. Prefer states with lower `f(n)` values.
7. Continue until the goal is reached.
8. Return the path to the goal.

### Think About

Compare the information used by each algorithm:

| Algorithm | Information Used |
|---|---|
| BFS | Search depth / frontier order |
| Greedy Best-First | `h(n)` |
| A* | `g(n) + h(n)` |

How might these differences affect the states each algorithm explores?

# Part D — Compare BFS and A*

Run BFS and A* on the **same grid**, using the same:

- Start state
- Goal state
- Obstacles

Record your results.

| Algorithm | Path Length | Explored States | Time (optional) |
|---|---:|---:|---:|
| BFS | | | |
| A* | | | |

## Discussion

Compare the behaviour of the two algorithms.

Consider:

- Do both algorithms find a path?
- Do they return paths of the same length?
- Which algorithm explores fewer states in your experiment?
- Why does their search behaviour differ?
- What additional information does A* have that BFS does not?

When comparing algorithms, be precise about what you mean by **performance**.

For example, you might compare:

- Path length
- Number of explored states
- Execution time

Different measures can produce different comparisons.

# Part E — Understanding the Heuristic

The heuristic is an important part of informed search.

Consider Manhattan Distance again:

```text
h(n) = |x₁ - x₂| + |y₁ - y₂|
```

It provides information about the estimated distance to the goal.

However, the heuristic does not necessarily know everything about the environment.

For example, consider what happens when obstacles lie between the current state and the goal.

### Questions

1. Does Manhattan Distance know where the obstacles are?
2. Can a state have a low heuristic value but still require a longer path to reach the goal?
3. What characteristics might make a heuristic useful?
4. What could happen if the heuristic provides poor guidance?

# Extension Tasks

Complete these only after finishing the main lab tasks.

## Extension 1 — Alternative Heuristics

Implement **Euclidean Distance**:

```text
distance = √((x₂ - x₁)² + (y₂ - y₁)²)
```

Run the search using:

- Manhattan Distance
- Euclidean Distance

Record your observations.

| Heuristic | Path Length | Explored States |
|---|---:|---:|
| Manhattan Distance | | |
| Euclidean Distance | | |

### Questions

- Do the heuristics cause the algorithm to explore the same states?
- Which heuristic explores fewer states in your experiment?
- Why might the choice of heuristic affect the search?

## Extension 2 — Larger Grid

Increase the grid size to:

```text
20 × 20
```

Compare:

- BFS
- Greedy Best-First Search
- A*

Record your results.

| Algorithm | Path Length | Explored States |
|---|---:|---:|
| BFS | | |
| Greedy Best-First | | |
| A* | | |

### Questions

- How does increasing the size of the state space affect the algorithms?
- Which algorithms explore the most states in your experiment?
- How useful does the heuristic become as the grid becomes larger?

## Extension 3 — Poor Heuristics

Create a deliberately uninformative heuristic.

For example:

```python
def heuristic(state, goal):
    return 0
```

Run A* using this heuristic.

Compare it with A* using Manhattan Distance.

### Questions

- What happens when `h(n)` is always `0`?
- What does the A* formula become?

Remember:

```text
f(n) = g(n) + h(n)
```

If:

```text
h(n) = 0
```

then:

```text
f(n) = g(n)
```

Observe how this changes the search behaviour.

How does the number of explored states compare with A* using Manhattan Distance?

# Reflection Questions

Be prepared to discuss:

1. What is the difference between uninformed and informed search?
2. Why is A* considered an informed search algorithm?
3. Why does BFS not need a heuristic?
4. What is a heuristic?
5. What does `h(n)` represent?
6. What does `g(n)` represent?
7. What does `f(n)` represent in A*?
8. How does Greedy Best-First Search differ from A*?
9. What makes a heuristic useful?
10. How can obstacles affect the usefulness of a heuristic?
11. What happened when you used `h(n) = 0`?
12. How did BFS and A* compare in your experiments?
13. What parts of the Week 2 search code were reused or repeated this week?
14. As we add more search algorithms, what problems might arise from keeping each problem and search implementation tightly connected?

# Demo Requirements

You should be able to demonstrate and explain:

- Your Manhattan Distance calculation.
- Greedy Best-First Search.
- A* Search.
- The meaning of `g(n)`, `h(n)`, and `f(n)`.
- A comparison between BFS and A*.
- The results of your experiments.
- The main differences between uninformed and informed search.

You should also be prepared to answer questions about your implementation.

# Summary

In Week 2, we explored the state space using uninformed search:

```text
BFS / DFS
    ↓
No estimate of distance to goal
    ↓
Explore according to frontier strategy
```

This week, we introduced **informed search**:

```text
Current State
      ↓
Generate Candidates
      ↓
Use Heuristic Information
      ↓
Choose What to Explore Next
```

Greedy Best-First Search uses:

```text
h(n)
```

and prefers states that appear closer to the goal.

A* uses:

```text
f(n) = g(n) + h(n)
```

and combines the cost of the path already travelled with an estimate of the remaining cost.

The progression so far is:

```text
Week 1
Problem Formulation
      ↓
Week 2
Uninformed Search
BFS and DFS
      ↓
Week 3
Informed Search
Greedy and A*
```

As we add more problems and more algorithms, you should also begin to notice that some ideas are repeated across our programs:

- Initial states
- Goal states
- Possible moves
- State transitions
- Goal tests
- Search algorithms

In the next lab, we will look at how some of these ideas can be organised into a more reusable structure.

## My answers

1. Uninformed search like BFS and DFS has no estimate of how close a state is to the goal. Informed search uses a heuristic to guide it.
2. A* is informed because it uses h(n), an estimate of the remaining cost to the goal.
3. BFS doesn't need a heuristic because it already explores systematically, level by level.
4. A heuristic is an estimate of how far a state is from the goal, or how much cost is left.
5. h(n) is that estimate of the remaining cost from n to the goal. I used Manhattan distance.
6. g(n) is the cost of the path so far, so the number of steps already taken to reach n.
7. f(n) is g(n) + h(n), the estimated total cost of the path going through n.
8. Greedy only uses h(n), so it always heads towards whatever looks closest. A* uses g + h, so it doesn't forget about the path already taken.
9. A useful heuristic is cheap to calculate, close to the true cost, and ideally never overestimates if you want A* to stay optimal.
10. Obstacles don't change the heuristic itself, because Manhattan distance ignores walls. That can make a low h misleading if a wall is in the way.
11. I didn't put h=0 in the file, but if h is always 0 then f is just g, so A* acts like uniform-cost search, which is the same as BFS on this grid. I tried it and it also expanded 93 states and still found the 18 move path.
12. Greedy and A* both found the same 18 move path, along the top then down the right. That's optimal because Manhattan from start to goal is 18. Greedy expanded 19 states. A* and BFS both expanded all 93 free cells. A* still has h, but a lot of cells have the same f value as 18, so it doesn't skip much on this grid.
13. I reused neighbours, parents, and reconstruct_path from week 2. Only the frontier ranking is new.
14. If every problem and search stay tightly mixed, you end up rewriting the same search for every new problem.

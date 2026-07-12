# MDP Problem Solving Assignment

## Course

Applied Machine Intelligence
Summer 2026 – Second Bi-Term

## Overview

This assignment demonstrates the solution of a deterministic Markov Decision Process using Bellman equations and dynamic programming techniques.

The notebook covers:

1. One-step Bellman expectation backup
2. Iterative policy evaluation
3. One iteration of value iteration
4. Optimal policy determination
5. Conceptual reasoning about MDPs
6. Analysis of a modified transition model

The discount factor used throughout the assignment is:

[
\gamma = 0.9
]

## MDP Description

The MDP contains three states:

* `S0`
* `S1`
* `S2`, which is terminal

Two actions are available:

* `A0`
* `A1`

### Transition and Reward Model

| Current State | Action | Next State | Reward |
| ------------- | ------ | ---------- | -----: |
| S0            | A0     | S1         |      5 |
| S0            | A1     | S2         |      2 |
| S1            | A0     | S2         |      4 |
| S1            | A1     | S0         |      1 |
| S2            | A0     | S2         |      0 |
| S2            | A1     | S2         |      0 |

### Fixed Policy

| State | Policy Action              |
| ----- | -------------------------- |
| S0    | A0                         |
| S1    | A1                         |
| S2    | Terminal-equivalent action |

## Main Results

### Problem 1: One-Step Bellman Expectation Backup

Starting from zero state values:

| State | Updated Value |
| ----- | ------------: |
| S0    |           5.0 |
| S1    |           1.0 |
| S2    |           0.0 |

### Problem 2: Policy Evaluation

Policy evaluation converged after 235 iterations using a tolerance of (10^{-10}).

| State | Converged Policy Value |
| ----- | ---------------------: |
| S0    |              31.052632 |
| S1    |              28.947368 |
| S2    |               0.000000 |

The fixed policy creates a continuing cycle between `S0` and `S1`, allowing the agent to repeatedly collect discounted rewards.

### Problem 3: First Value-Iteration Backup

| State | Q(S, A0) | Q(S, A1) | Updated Value |
| ----- | -------: | -------: | ------------: |
| S0    |      5.0 |      2.0 |           5.0 |
| S1    |      4.0 |      1.0 |           4.0 |
| S2    |      0.0 |      0.0 |           0.0 |

### Problem 4: Optimal Policy

| State | Q*(S, A0) | Q*(S, A1) | Optimal Action |
| ----- | --------: | --------: | -------------- |
| S0    | 31.052632 |  2.000000 | A0             |
| S1    |  4.000000 | 28.947368 | A1             |
| S2    |  0.000000 |  0.000000 | Terminal       |

The optimal policy is:

[
\pi^*(S_0)=A_0
]

[
\pi^*(S_1)=A_1
]

Although action `A0` in `S1` provides a larger immediate reward, action `A1` is optimal because it returns the agent to `S0`, allowing additional future rewards.

### Problem 5: Concept Check

The conceptual section discusses:

* Reward hacking caused by poorly designed reward functions
* The difference between expectation and maximization in Bellman equations
* The role of terminal states as boundary conditions in dynamic programming

### Problem 6: Modified Transition

The transition for `S1` with action `A0` was conceptually changed from:

```text
S1 → S2 with reward 4
```

to:

```text
S1 → S0 with reward 3
```

This change:

* Increases the long-term value of `S1`
* Changes the optimal action in `S1` to `A0`
* Makes the MDP more cyclic
* Encourages the agent to remain in the `S0–S1` reward cycle

## Validation

The notebook programmatically validates:

* Converged policy-evaluation values
* The first value-iteration backup
* The final greedy optimal policy

All validation checks returned `True`.

## Technologies Used

* Python
* Jupyter Notebook
* pandas

## Project Files

```text
Assignment_MDP_Problem_Solving/
├── MDP_Problem_Solving.ipynb
├── README.md
└── outputs/
```

## Conclusion

This assignment demonstrates how Bellman expectation equations evaluate a fixed policy, while Bellman optimality equations compare actions to identify optimal behavior. It also illustrates why long-term discounted returns can make an action with a smaller immediate reward preferable to an action that terminates the process.

# Bellman Equations Programming Assignment

## Course

Applied Machine Intelligence
Summer 2026 – Second Bi-Term

## Project Overview

This assignment demonstrates the implementation of the Bellman expectation equation and Bellman optimality equation for a small Markov Decision Process (MDP).

The notebook calculates and interprets:

* state-value functions (V^\pi(s));
* action-value functions (Q^\pi(s,a));
* optimal state values (V^*(s));
* optimal action values (Q^*(s,a));
* an optimal policy derived through value iteration.

The notebook also tracks value estimates across iterations, verifies convergence, and demonstrates how changing a reward affects the computed values.

## Project Structure

```text
Assignment_Bellman_Equations/
├── Bellman_Equations_Programming_Assignment.ipynb
├── README.md
├── outputs/
└── screenshots/
```

## Markov Decision Process

The environment contains three states:

* `S0`
* `S1`
* `S2`

The available actions are:

* `A0`
* `A1`

State `S2` is treated as a terminal state.

The discount factor used in the calculations is:

```text
gamma = 0.9
```

### Transition and Reward Structure

| Current State | Action | Next State | Probability | Reward |
| ------------- | ------ | ---------- | ----------: | -----: |
| S0            | A0     | S1         |         1.0 |    5.0 |
| S0            | A1     | S2         |         1.0 |    2.0 |
| S1            | A0     | S2         |         1.0 |    4.0 |
| S1            | A1     | S0         |         1.0 |    1.0 |
| S2            | A0     | S2         |         1.0 |    0.0 |
| S2            | A1     | S2         |         1.0 |    0.0 |

## Fixed Policy

The fixed policy selects:

* `A0` in `S0`;
* `A1` in `S1`;
* either action in terminal state `S2`.

## Bellman Expectation Results

Iterative policy evaluation converged after 192 iterations using a tolerance of (10^{-8}).

| State | (V^\pi(s)) |
| ----- | ---------: |
| S0    |    31.0526 |
| S1    |    28.9474 |
| S2    |     0.0000 |

The action-value function under the fixed policy was:

| State | (Q^\pi(s,A0)) | (Q^\pi(s,A1)) |
| ----- | ------------: | ------------: |
| S0    |       31.0526 |        2.0000 |
| S1    |        4.0000 |       28.9474 |
| S2    |        0.0000 |        0.0000 |

## Bellman Optimality Results

Value iteration converged after 189 iterations.

| State | (V^*(s)) |
| ----- | -------: |
| S0    |  31.0526 |
| S1    |  28.9474 |
| S2    |   0.0000 |

The optimal action-value function was:

| State | (Q^*(s,A0)) | (Q^*(s,A1)) |
| ----- | ----------: | ----------: |
| S0    |     31.0526 |      2.0000 |
| S1    |      4.0000 |     28.9474 |
| S2    |      0.0000 |      0.0000 |

The optimal policy was:

| State | Optimal Action |
| ----- | -------------- |
| S0    | A0             |
| S1    | A1             |
| S2    | A0 or A1       |

Both actions in `S2` have a value of zero because it is terminal.

The fixed policy produced the same state values as the optimal policy, demonstrating that the supplied policy was already optimal for this MDP.

## Reward Modification Experiment

The reward for the transition:

```text
S0 --A0--> S1
```

was increased from 5 to 8.

The modified values were:

| State | Original (V^*(s)) | Modified (V^*(s)) |  Change |
| ----- | ----------------: | ----------------: | ------: |
| S0    |           31.0526 |           46.8421 | 15.7895 |
| S1    |           28.9474 |           43.1579 | 14.2105 |
| S2    |            0.0000 |            0.0000 |  0.0000 |

The optimal actions did not change. However, the values of both `S0` and `S1` increased because the states are connected through a repeating transition cycle.

## Key Concepts Demonstrated

* Markov Decision Processes
* states, actions, transitions, and rewards
* policies
* discount factor
* Bellman expectation equation
* Bellman optimality equation
* iterative policy evaluation
* value iteration
* state-value functions
* action-value functions
* convergence
* optimal policy extraction

## Central Bellman Relationship

```text
Current Value = Immediate Reward + Discounted Future Value
```

The Bellman expectation equation evaluates a specified policy, while the Bellman optimality equation selects the action with the highest expected long-term return.

## Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Jupyter Notebook

## Running the Notebook

1. Open `Bellman_Equations_Programming_Assignment.ipynb`.
2. Select a Python environment containing NumPy, Pandas, and Matplotlib.
3. Run all cells from top to bottom.
4. Confirm that all tables, validation results, and convergence plots are displayed.
5. Verify that no cells produce errors.

## AI Use Disclosure

ChatGPT was used to help explain Bellman equations, organize the notebook, develop and review the Python implementation, and improve the clarity of code comments and interpretations. All code, calculations, and outputs were reviewed and executed by the student to verify correctness and support personal understanding of the assignment.

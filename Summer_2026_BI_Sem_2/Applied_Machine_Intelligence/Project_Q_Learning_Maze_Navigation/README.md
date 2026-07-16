# Q-Learning for Grid-Based Maze Navigation

## Project Overview

This project implements the Q-learning reinforcement learning algorithm in a grid-based maze environment. The agent learns how to move from a starting location to a goal by repeatedly interacting with the maze, receiving rewards and penalties, and updating a Q-table.

The project demonstrates:

* A grid-based maze environment
* States, actions, rewards, walls, and terminal conditions
* Epsilon-greedy exploration
* The Q-learning update rule
* Training-progress tracking
* Learned-policy extraction
* Optimal-path evaluation
* Hyperparameter comparison
* Convergence and performance visualizations

All implementation, analysis, explanations, and results are contained in the Jupyter Notebook:

```text
q_learning_maze.ipynb
```

---

## Project Structure

```text
Project_Q_Learning_Maze_Navigation/
│
├── outputs/
│   ├── baseline_episode_rewards.png
│   ├── baseline_performance_comparison.csv
│   ├── baseline_q_value_convergence.png
│   ├── baseline_rolling_steps.png
│   ├── baseline_rolling_success_rate.png
│   ├── baseline_training_history.csv
│   ├── final_q_table.csv
│   ├── greedy_policy_evaluation.csv
│   ├── hyperparameter_convergence_speed.png
│   ├── hyperparameter_experiment_summary.csv
│   ├── hyperparameter_reward_comparison.png
│   ├── hyperparameter_success_comparison.png
│   └── learned_policy.csv
│
├── screenshots/
├── q_learning_maze.ipynb
└── README.md
```

---

## Maze Environment

The environment is a 5 × 5 grid containing:

* Start state: `(4, 0)`
* Goal state: `(0, 4)`
* Trap state: `(4, 4)`
* Six blocked cells or walls
* Nineteen valid states
* Four possible actions:

  * Up
  * Down
  * Left
  * Right

### Maze Layout

|       | Col 0 | Col 1 | Col 2 | Col 3 | Col 4 |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Row 0 | .     | #     | .     | .     | G     |
| Row 1 | .     | #     | .     | #     | .     |
| Row 2 | .     | .     | .     | #     | .     |
| Row 3 | .     | #     | #     | .     | .     |
| Row 4 | S     | .     | .     | .     | T     |

Legend:

* `S` = Start
* `G` = Goal
* `T` = Trap
* `#` = Wall
* `.` = Open state

---

## Reward Structure

| Event            | Reward |
| ---------------- | -----: |
| Reach the goal   |   +100 |
| Enter the trap   |    −50 |
| Valid movement   |     −1 |
| Invalid movement |     −5 |

An invalid movement occurs when the agent attempts to move outside the grid or into a wall. In this situation, the agent remains in its current state.

The goal and trap are terminal states and end the current episode.

---

## Q-Learning Algorithm

The agent updates its state-action values using the Q-learning equation:

[
Q(s,a) \leftarrow Q(s,a) + \alpha
\left[r + \gamma \max_{a'}Q(s',a') - Q(s,a)\right]
]

Where:

* (Q(s,a)) is the current Q-value.
* (\alpha) is the learning rate.
* (r) is the immediate reward.
* (\gamma) is the discount factor.
* (\max Q(s',a')) is the highest estimated future value from the next state.

For terminal states, the future Q-value is zero.

---

## Epsilon-Greedy Exploration

The agent uses an epsilon-greedy strategy to balance exploration and exploitation.

* With probability (\epsilon), the agent selects a random action.
* With probability (1-\epsilon), the agent selects an action with the highest known Q-value.
* When multiple actions have the same maximum Q-value, the agent randomly selects among the tied actions.

Epsilon begins at `1.0`, allowing extensive exploration at the beginning of training, and gradually decreases to a minimum of `0.05`.

---

## Baseline Hyperparameters

| Hyperparameter            | Value |
| ------------------------- | ----: |
| Learning rate, α          |  0.10 |
| Discount factor, γ        |  0.95 |
| Initial epsilon           |  1.00 |
| Minimum epsilon           |  0.05 |
| Epsilon decay             | 0.995 |
| Training episodes         | 2,000 |
| Maximum steps per episode |   100 |
| Random seed               |    42 |

An episode ends when the agent:

* Reaches the goal
* Enters the trap
* Reaches the maximum number of allowed steps

---

## Baseline Results

The baseline agent achieved the following results:

| Metric                               |       Result |
| ------------------------------------ | -----------: |
| Overall training success rate        |       98.25% |
| First 100 episodes success rate      |          65% |
| Last 100 episodes success rate       |         100% |
| Episode reaching 90% rolling success |          144 |
| Final greedy-policy steps            |            8 |
| Final greedy-policy reward           |           93 |
| Final greedy-policy outcome          | Goal reached |

The learned policy reached the goal using the following path:

```text
(4, 0)
→ (3, 0)
→ (2, 0)
→ (2, 1)
→ (2, 2)
→ (1, 2)
→ (0, 2)
→ (0, 3)
→ (0, 4)
```

The agent completed the route in eight actions. This is the shortest possible path between the start and goal positions in the maze.

The evaluation reward was:

[
7(-1) + 100 = 93
]

The agent received seven movement penalties before receiving the goal reward.

---

## Learned Q-Values

The learned Q-table showed behavior consistent with the maze structure.

At the start state `(4, 0)`, the learned Q-values were:

| Action | Q-value |
| ------ | ------: |
| Up     |  63.800 |
| Down   |  55.374 |
| Left   |  55.396 |
| Right  |  55.093 |

The agent selected `UP` because it had the highest expected long-term value.

At state `(0, 3)`, moving `RIGHT` had a Q-value of `100` because the action immediately reached the goal.

At state `(4, 3)`, moving `RIGHT` had a strongly negative Q-value because it entered the trap.

---

## Hyperparameter Experiments

Six configurations were tested:

1. Baseline
2. Low learning rate
3. High learning rate
4. Low discount factor
5. Fast epsilon decay
6. Slow epsilon decay

### Experiment Summary

| Configuration       | Episode to 90% Success | First 100 Success | Last 100 Success | Greedy Steps | Greedy Reward |
| ------------------- | ---------------------: | ----------------: | ---------------: | -----------: | ------------: |
| Baseline            |                    144 |               65% |             100% |            8 |            93 |
| Low Learning Rate   |                    180 |               44% |             100% |            8 |            93 |
| High Learning Rate  |                    113 |               79% |             100% |            8 |            93 |
| Low Discount Factor |                    156 |               57% |             100% |            8 |            93 |
| Fast Epsilon Decay  |                    110 |               84% |             100% |            8 |            93 |
| Slow Epsilon Decay  |                    280 |               38% |             100% |            8 |            93 |

All configurations eventually learned the same optimal eight-action policy. However, they differed in learning speed and convergence behavior.

### Main Findings

* The fast epsilon-decay configuration reached 90% rolling success earliest, at episode 110.
* The high learning-rate configuration reached 90% success at episode 113 and showed stable final Q-values.
* The low learning rate learned more slowly because Q-values were updated gradually.
* The low discount factor placed less value on future rewards and learned slightly more slowly than the baseline.
* The slow epsilon-decay configuration continued exploring for longer and required 280 episodes to reach 90% rolling success.
* The baseline configuration provided a balanced combination of exploration, learning speed, and convergence.

---

## Generated Visualizations

The notebook creates and saves the following plots:

* Episode rewards over time
* Rolling average reward
* Rolling average steps
* Rolling success rate
* Q-value convergence
* Hyperparameter reward comparison
* Hyperparameter success-rate comparison
* Episodes required to reach 90% success

These plots are stored in the `outputs` directory.

---

## Technologies Used

* Python
* Jupyter Notebook
* NumPy
* Pandas
* Matplotlib

---

## Running the Project

### 1. Open the project folder

```powershell
cd C:\Users\dubey\Documents\UC_GitLab\Summer_2026_BI_Sem_2\Applied_Machine_Intelligence\Project_Q_Learning_Maze_Navigation
```

### 2. Open the notebook in VS Code

```powershell
code q_learning_maze.ipynb
```

### 3. Select the Python environment

Select the project’s Python or `.venv_global` Jupyter kernel.

### 4. Run the notebook

Run all cells in order from the beginning.

The notebook will:

* Create the maze environment
* Validate movement and reward rules
* Initialize the Q-table
* Train the baseline agent
* Evaluate the learned policy
* Run hyperparameter experiments
* Generate plots
* Save tables and results to the `outputs` folder

---

## Reproducibility

A fixed random seed of `42` is used for Python and NumPy. This helps produce consistent results when the notebook is rerun under the same environment and library versions.

---

## Conclusion

This project demonstrates that Q-learning can learn an optimal maze-navigation strategy through repeated interaction with an environment. The agent was not provided with the correct route in advance. Instead, it learned through exploration, rewards, penalties, and repeated updates to its Q-table.

The trained agent successfully learned the shortest eight-action route from the starting state to the goal. The hyperparameter experiments also demonstrated that learning rate, discount factor, and epsilon decay affect how quickly and smoothly the agent learns, even when the final optimal policy is the same.

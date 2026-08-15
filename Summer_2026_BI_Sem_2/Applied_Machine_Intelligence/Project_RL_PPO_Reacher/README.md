@'
# Reinforcement Learning Project Part 2: PPO-Based Robotic Arm Control

## Project Overview

This project implements a Proximal Policy Optimization (PPO) reinforcement learning agent for continuous control of a two-joint robotic arm in the MuJoCo `Reacher-v5` environment.

The goal is to train an agent to apply continuous torque values to two robotic joints so that the robotic fingertip moves closer to a randomly positioned target while minimizing unnecessary control effort.

## Environment

- Environment: `Reacher-v5`
- Simulator: MuJoCo
- Observation space: 10 continuous features
- Action space: 2 continuous torque values
- Episode length: 50 steps

## Algorithm

The project uses PPO with an actor-critic neural network.

The actor learns a Gaussian continuous-action policy, while the critic estimates the state-value function. Generalized Advantage Estimation (GAE) is used to calculate advantages, and PPO clipping is used to stabilize policy updates.

## Tools and Libraries

- Python 3.11.9
- Gymnasium 1.3.0
- MuJoCo 3.11.0
- PyTorch 2.10.0 CPU
- NumPy
- Pandas
- Matplotlib
- ImageIO

## Hyperparameters

| Hyperparameter | Value |
|---|---:|
| Learning rate | 0.0003 |
| Gamma | 0.99 |
| GAE lambda | 0.95 |
| PPO clip epsilon | 0.20 |
| Rollout steps | 1,024 |
| Minibatch size | 64 |
| PPO epochs | 10 |
| Entropy coefficient | 0.01 |
| Value coefficient | 0.50 |
| Max gradient norm | 0.50 |
| Training updates | 100 |
| Total environment steps | 102,400 |

## Final Results

| Metric | Result |
|---|---:|
| Random baseline reward | -42.8072 |
| PPO evaluation reward | -7.9557 |
| Reward improvement | +34.8515 |
| Random mean target distance | 0.1857 |
| PPO mean target distance | 0.1488 |
| Target distance reduction | 19.87% |
| Random mean control cost | 0.6705 |
| PPO mean control cost | 0.0103 |
| Control cost reduction | 98.46% |
| Evaluation success rate | 10.00% |
| Success threshold | 0.05 |
| Training runtime | 129.50 seconds |

## Key Findings

The trained PPO agent substantially outperformed the random-action baseline. The evaluation reward improved from -42.8072 to -7.9557. The agent also reduced the mean fingertip-to-target distance by 19.87% and reduced control effort by 98.46%.

The results show that PPO learned a more effective and efficient continuous-control policy for the Reacher-v5 robotic arm.

## Project Structure

```text
Project_RL_PPO_Reacher/
│
├── RL_PPO_Reacher_Project.ipynb
├── README.md
│
├── checkpoints/
│   └── ppo_reacher_final.pt
│
├── outputs/
│   ├── random_baseline_metrics.csv
│   ├── random_baseline_summary.csv
│   ├── ppo_training_episode_metrics.csv
│   ├── ppo_training_update_metrics.csv
│   ├── ppo_training_summary.csv
│   ├── ppo_evaluation_episode_metrics.csv
│   ├── ppo_evaluation_summary.csv
│   ├── random_vs_ppo_comparison.csv
│   └── *.png
│
├── screenshots/
│   ├── ppo_demo_initial.png
│   ├── ppo_demo_middle.png
│   └── ppo_demo_final.png
│
├── demo/
│   ├── ppo_reacher_trained_agent.mp4
│   └── ppo_reacher_presentation_demo.mp4
│
└── presentation/
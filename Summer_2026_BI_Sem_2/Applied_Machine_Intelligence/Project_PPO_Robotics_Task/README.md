# PPO for Continuous Control Robotics

## Project Overview

This project implements Proximal Policy Optimization (PPO) from scratch using PyTorch for a continuous-control robotics task.

The agent is trained in the Gymnasium MuJoCo `Reacher-v5` environment. The objective is to control a two-joint robotic arm so that its fingertip moves toward a target while avoiding unnecessarily large control actions.

The implementation includes:

- Continuous-control MuJoCo robotics environment
- Actor-Critic neural network architecture
- Gaussian continuous-action policy
- Tanh-bounded robot actions
- PPO clipped surrogate objective
- Generalized Advantage Estimation (GAE)
- Advantage normalization
- Mini-batch optimization
- Multiple PPO epochs per rollout
- Entropy-based exploration
- Gradient clipping
- Training metrics and visualizations
- Deterministic final-policy evaluation
- Model checkpointing

---

## Environment

The project uses:

- **Environment:** `Reacher-v5`
- **Framework:** Gymnasium
- **Physics simulator:** MuJoCo
- **Deep learning framework:** PyTorch
- **Python:** 3.11.9
- **Gymnasium:** 1.3.0
- **MuJoCo:** 3.11.0
- **PyTorch:** 2.10.0+cpu

The Reacher environment provides:

- **Observation dimension:** 10
- **Action dimension:** 2
- **Action range:** `[-1, 1]`

The observation represents information about the robotic arm configuration, target position, joint velocities, and fingertip-to-target displacement.

---

## Actor-Critic Architecture

Both the actor and critic use fully connected neural networks with two hidden layers.

### Actor

```text
State (10)
   ↓
Linear 64
   ↓
Tanh
   ↓
Linear 64
   ↓
Tanh
   ↓
Action Mean (2)
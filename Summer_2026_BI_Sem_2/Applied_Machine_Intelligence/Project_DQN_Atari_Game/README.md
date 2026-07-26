# DQN on Atari Breakout

## Project Overview

This project implements a Deep Q-Network (DQN) agent for the Atari game **Breakout** using PyTorch and the Gymnasium-compatible Arcade Learning Environment (ALE). The notebook demonstrates the complete DQN pipeline from raw visual observations through preprocessing, experience collection, neural-network training, target-network synchronization, checkpointing, visualization, and evaluation.

The implementation was developed and executed locally in the shared `.venv_global` Python environment on a CPU. The selected environment is:

```text
ALE/Breakout-v5
```

## Main DQN Components

The notebook includes all required project components:

- Atari Breakout environment
- Grayscale conversion and resizing to 84 x 84 pixels
- Four-frame stacking
- Convolutional neural network for Q-value approximation
- Experience replay buffer
- Online and target networks
- Epsilon-greedy exploration
- Bellman target calculation
- Huber loss and gradient clipping
- Target-network synchronization
- Model checkpointing
- Episode reward, loss, Q-value, and TD-error tracking
- Random-baseline and trained-agent evaluation
- Gameplay screenshots

## Project Structure

```text
Project_DQN_Atari_Game/
├── DQN_Atari_Game.ipynb
├── README.md
├── checkpoints/
│   └── breakout_dqn_local_final.pt
├── outputs/
│   ├── breakout_dqn_local_episode_metrics.csv
│   ├── breakout_dqn_local_update_metrics.csv
│   ├── breakout_dqn_local_summary.json
│   ├── epsilon_schedule.png
│   ├── local_episode_reward_curve.png
│   ├── local_training_loss_curve.png
│   ├── local_q_value_trends.png
│   ├── local_td_error_curve.png
│   ├── local_evaluation_metrics.csv
│   ├── local_evaluation_comparison.png
│   └── final_project_summary.json
├── screenshots/
│   ├── raw_breakout_frame.png
│   ├── preprocessed_stacked_frames.png
│   └── trained_dqn_best_evaluation_frame.png
└── report/
    └── DQN_Atari_Game_Report.docx
```

## Environment and Dependencies

The local run used:

- Python 3.11.9
- PyTorch 2.10.0
- Gymnasium 1.3.0
- ALE-Py 0.12.0
- NumPy 1.26.4
- OpenCV 4.10.0.84
- Matplotlib 3.10.8
- Pandas 2.3.3

Install the main project dependencies with:

```bash
python -m pip install "gymnasium[atari]" opencv-python==4.10.0.84 torch numpy pandas matplotlib
```

## Running the Notebook

1. Open `DQN_Atari_Game.ipynb` in VS Code or Jupyter.
2. Select the `.venv_global` kernel.
3. Run the notebook cells from top to bottom.
4. The notebook automatically detects the local runtime and selects the CPU device when CUDA is unavailable.
5. Generated checkpoints, plots, metrics, and screenshots are saved in their corresponding project folders.

## Local Training Configuration

| Hyperparameter | Value |
|---|---:|
| Environment steps | 8,000 |
| Approximate Atari frames | 32,000 |
| Learning rate | 0.0001 |
| Discount factor | 0.99 |
| Batch size | 32 |
| Replay capacity | 5,000 |
| Learning starts | 1,000 steps |
| Training frequency | Every 4 steps |
| Target update frequency | Every 1,000 steps |
| Epsilon schedule | 1.00 to 0.10 |
| Epsilon decay period | 6,000 steps |
| Gradient clipping norm | 10.0 |

## Key Results

The local CPU run produced the following results:

- Completed episodes: **37**
- Optimization updates: **1,751**
- Target-network synchronizations: **8**
- Mean training episode reward: **1.4324**
- Best training episode reward: **6.0**
- First 10-episode mean reward: **1.0**
- Final 10-episode mean reward: **1.3**
- Mean training loss: **0.003766**
- Final 100-update mean loss: **0.003008**
- Final 100-update mean TD error: **0.037163**
- Random-baseline evaluation mean reward: **1.1**
- Trained-DQN evaluation mean reward: **1.1**

The network demonstrated stable numerical learning behavior. Training loss and temporal-difference error decreased, and predicted Q-values remained close to the Bellman targets. The episode reward showed limited improvement, but the trained policy did not outperform the random baseline in average evaluation reward. Therefore, the short local run validates the complete DQN implementation but does not demonstrate stable policy convergence.

## Limitations

The training run was intentionally limited to 8,000 environment steps so it could be completed locally on a CPU. Atari DQN agents typically require substantially more interaction data and computation to achieve reliable performance. The local results should therefore be interpreted as a functional demonstration rather than a fully converged Breakout agent.

## References

- Mnih, V., Kavukcuoglu, K., Silver, D., et al. (2015). Human-level control through deep reinforcement learning. *Nature, 518*, 529-533. https://doi.org/10.1038/nature14236
- Gymnasium Documentation. Breakout Atari environment. https://gymnasium.farama.org/environments/atari/breakout/
- PyTorch Documentation. SmoothL1Loss. https://docs.pytorch.org/docs/stable/generated/torch.nn.SmoothL1Loss.html
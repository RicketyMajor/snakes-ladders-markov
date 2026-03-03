# Snakes & Ladders: Markov Chain Modeling

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![Math](https://img.shields.io/badge/Math-Stochastic_Processes-orange.svg)

## Project Overview
This repository contains a mathematical and computational modeling of the classic board game **Snakes and Ladders** using **Discrete-Time Markov Chains (DTMC)**. 

The main goal of this project is to translate the rules of the game (including complex mechanics like repeating turns on a 6, exact-arrival bouncing, and trap chaining) into a rigorous stochastic process to extract theoretical metrics such as the stationary distribution and the expected game duration.

## Objectives
* **Objective A:** Construct the $50 \times 50$ Transition Matrix ($P$) taking into account complex turn structures.
* **Objective B:** Calculate the stationary vector $\pi$ using three different approaches (Exact Linear System, Power Iteration, and Monte Carlo Random Walk) and analyze its convergence.
* **Objective C:** Compute the expected duration of a single game using the Fundamental Matrix.
* **Objective D:** Analyze the expected visits per state to identify bottlenecks and trap distributions.

## Mathematical Foundation
The core of this project relies on decomposing a player's turn into a series of sub-turns (due to the "roll a 6 to roll again" rule). The final transition matrix is computed as an infinite geometric series that converges to:
$$P = (I - B)^{-1} A$$
Where $A$ contains the probabilities of ending a turn, and $B$ contains the probabilities of continuing a turn. Furthermore, metrics for a single game are extracted using the **Fundamental Matrix** $N = (I - Q)^{-1}$, where $Q$ is the submatrix of transient states.

## Repository Structure
```text
snakes-ladders-markov/
├── config/
│   └── board_config.yaml         # Game rules, board size, snakes, and ladders
├── notebooks/                    # Data Science & Theoretical Analysis
│   ├── 01_matrix_construction.ipynb
│   ├── 02_pi_vector_calculation.ipynb
│   └── 03_game_metrics.ipynb
├── src/                          # Core Python Backend
│   ├── board.py                  # Board logic and trap triggers
│   ├── markov.py                 # Transition matrix generation
│   ├── solvers.py                # Mathematical solvers for pi vector
│   └── metrics.py                # Fundamental matrix and absorption metrics
└── tests/                        # Unit testing (Pytest)
    ├── test_markov.py
    └── test_solvers.py
```

## Installation & Setup (Linux/Ubuntu)

To run this project locally, follow these steps:

1. **Clone the repository:**

```bash
git clone [https://github.com/YOUR_USERNAME/snakes-ladders-markov.git](https://github.com/YOUR_USERNAME/snakes-ladders-markov.git)
cd snakes-ladders-markov
```

2. **Create and activate a virtual environment:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## Testing

This project strictly follows TDD (Test-Driven Development) principles. To ensure the mathematical integrity of the transition matrices and solvers, run:

```bash
python -m pytest
```

## Key Findings

- **Expected Game Duration:** The theoretical expected time to win a game on this specific 50-square board is 21.21 turns.The "Square 49" Bottleneck: Due to the exact-arrival rule, players get stuck at square 49 bouncing back, making it the most visited transient state in the game (averaging >2.5 visits per game).

- **Convergence:** Monte Carlo simulations (Random Walk) beautifully illustrate the Central Limit Theorem, converging to the exact analytical vector $\pi$ after $\approx 80,000$ steps.

## Future Work

Convert the environment into a Markov Decision Process (MDP).Implement a Reinforcement Learning agent (using Value Iteration or Q-Learning) to choose between different dice (e.g., a safe 3-sided die vs. a risky 6-sided die) to minimize the expected game duration.


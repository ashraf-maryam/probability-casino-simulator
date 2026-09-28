# Probability Casino Simulator

An interactive Python program that demonstrates six probability distributions through casino-style games and simulations.

This project was created for **Math 341: Probability & Statistics** and combines probability theory with programming. Each game simulates a random outcome and then calculates the theoretical probability of the result.

## Probability Distributions

| Distribution | Casino Game | Concept |
|---|---|---|
| Bernoulli | Coin Flip Table | One trial with two possible outcomes |
| Binomial | Multi-Flip Coin Game | Number of successes across independent trials |
| Hypergeometric | Ace Hunt Card Game | Sampling without replacement |
| Poisson | Slot Machine Jackpot | Number of rare events over repeated trials |
| Geometric | First Win Challenge | Trials required until the first success |
| Negative Binomial | Three Wins Challenge | Trials required to reach multiple successes |

## Features

- Interactive command-line menu
- Six probability-based casino games
- Random event simulation
- Theoretical probability calculations
- User-defined simulation parameters
- Comparison between simulated outcomes and probability models
- Modular Python functions for each distribution

## Technologies

- Python 3
- `random` module
- `math` module

No third-party packages are required.

## Run the Project

Clone the repository and run:

```bash
python3 casino_probability_simulator.py
```

Choose a game from the menu and follow the prompts.

## Example Menu

```text
==============================
🎲 PROBABILITY CASINO SIMULATOR
==============================
1. Coin Flip Table
2. Multi-Flip Coin Game
3. Ace Hunt Card Game
4. Slot Machine Jackpot
5. First Win Challenge
6. Three Wins Challenge
7. Leave Casino
```

## What I Learned

This project helped connect probability formulas to computational simulation. Building each game required identifying the assumptions behind the corresponding distribution and implementing those rules correctly in Python.

The project also strengthened my use of:

- Functions and modular program structure
- Loops and conditional logic
- Random simulation
- Probability calculations
- Input-driven program behavior
- Testing simulated outcomes against theoretical probability

## Project Context

**Course:** Math 341 — Probability & Statistics  
**Project:** Final Project  
**Language:** Python

The simulator was designed as an educational project to make probability distributions more interactive and intuitive.

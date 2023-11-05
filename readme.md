# Roulette Game

This is a simple text-based Roulette game written in Python. It allows the user to place bets on a number, color (red or black), or whether the number is even or odd.

## How to Play

- Start the game, and you will be prompted to place your bet.
- You can bet on a specific number between 0 and 36, or choose from the following options:
  - 'red' for a red number
  - 'black' for a black number
  - 'even' for an even number
  - 'odd' for an odd number
- The game will then simulate a spin of the roulette wheel and announce the result.
- If your bet matches the result, you win; otherwise, you lose.
- After each spin, you can choose to play again or exit the game.

## Installation

No installation is required. You just need to have Python installed on your system to run the script.

## Requirements

- Python 3.x

## Running the Game

To run the game, navigate to the directory containing the `roulette_game.py` script in your terminal and execute the following command:

```bash
python roulette_game.py
```

## Features

- The game uses `secrets.randbelow(37)` from Python's `secrets` module to simulate a random spin of the roulette wheel.
- The game covers multiple betting options - number, color, even, and odd.
- The game will continue running until you choose not to play anymore.

## Contributing

Feel free to fork the project, make changes, and submit a pull request if you have ideas on how to improve the game.

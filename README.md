# Dice Game 🎲

This repository contains an interactive, text-based Dice Game implemented in Python. The game is designed to provide a fun and engaging experience while showcasing fundamental programming principles, including modular design and file handling.

---

## Features

- **Interactive Gameplay**: The game is played between a human player and the computer.
- **Dynamic Dice Rolls**: Dice rolls determine player movement, with special rules for starting and moving.
- **Black Hole Mechanic**: Adds a strategic element where players landing on certain positions are sent back to the start.
- **Game Rules**: Players can view detailed rules before starting.
- **Replay Option**: Players can choose to play multiple rounds.
- **Result Tracking**: Game results, including the date and outcome, are saved to a text file.

---

## Gameplay Rules

1. The game starts when the human player rolls a 6.
2. Players move forward by half the dice roll value (rounded down).
3. Black holes are positioned at blocks 7 and 14. Landing on one resets the player's position to 1.
4. The first player to reach or exceed block 20 wins the game.
5. Game results include the total moves and black hole encounters for both players.

---

## Project Structure

The project is organized into modular Python files for readability and maintainability:


---

## Requirements

- **Python Version**: 3.11.2
- **Dependencies**: None (uses standard Python libraries)

---

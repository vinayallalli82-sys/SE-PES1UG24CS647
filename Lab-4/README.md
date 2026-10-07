# Lab 4 - VibeCoding

## Student Details

**Name:** A Vinay  
**SRN:** PES1UG24CS647

## Objective

To use Vibe Coding with an LLM to identify, fix, and improve an existing Endless Runner game by implementing the required features.

## Project

**Project:** Real-Time Endless Runner Game

The project is a terminal-based Endless Runner game developed using Python and Pygame.

## Tasks Completed

### Task 1 - Refine Collision Detection

Improved collision detection so that obstacles cannot unfairly pass through the player at higher speeds. The game speed is also limited to a maximum value to maintain fair gameplay.

### Task 2 - Game Over Condition

Added a graphical Game Over screen that displays the final score and provides instructions for the next action instead of only printing the result in the console.

### Task 3 - Replay Option

Added a replay system after Game Over with three difficulty levels:

- Easy
- Medium
- Hard

Each difficulty has a different starting speed and obstacle spawn rate. The game state is properly reset when starting a new game.

### Task 4 - Sound Feedback

Added sound effects for:

- Player jumping
- Scoring after passing an obstacle
- Game Over

## Technologies Used

- Python
- Pygame
- Git
- GitHub
- LLM / Vibe Coding

## Project Structure

```text
Lab-4/
├── 39_endless-runner/
│   ├── game/
│   │   ├── game_engine.py
│   │   ├── obstacle.py
│   │   └── player.py
│   ├── sounds/
│   │   ├── jump.wav
│   │   ├── score.mp3
│   │   └── game_over.mp3
│   ├── main.py
│   ├── README.md
│   └── requirements.txt
│
├── Before_Video.mp4
├── After_Video.mp4
└── README.md

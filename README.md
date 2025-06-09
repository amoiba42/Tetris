# Tetris Game

## Overview
This project is a fully functional Tetris game implemented with features such as scoring, increasing difficulty levels, and smooth game animations. It provides an engaging user experience while staying true to the classic Tetris gameplay mechanics.

## Features
- **Scoring System**: Tracks the player’s score based on lines cleared.
- **Increasing Difficulty**: The game becomes progressively faster as the player clears more lines.
- **Smooth Animations**: Ensures a seamless visual experience with fluid block movements and transitions.
- **Classic Gameplay**: Maintains the traditional rules of Tetris, including block rotation, line clearing, and game-over conditions.

## Technologies Used
- **Programming Language**: Python
- **Libraries**: Pygame (for graphics and input handling)

## Installation
To run the Tetris game, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/amoiba42/Tetris
   cd Tetris
   ```

2. **Install Dependencies**:
   Ensure you have Python installed (version 3.6 or higher). Then, install the required libraries:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   Execute the main script to start the game:
   ```bash
   python tetris.py
   ```

## How to Play
1. **Objective**:
   Arrange the falling blocks (Tetrominoes) to form complete horizontal lines. When a line is completed, it clears, and you score points.

2. **Controls**:
   - **Arrow Keys**: Move the block left or right
   - **Up Arrow**: Rotate the block
   - **Down Arrow**: Speed up the block’s descent
   - **Spacebar**: Instantly drop the block

3. **Game Progression**:
   - The game’s speed increases as you clear more lines.
   - The game ends when the blocks reach the top of the screen.

## Acknowledgments
- Inspired by the classic Tetris game developed by Alexey Pajitnov.
- Thanks to the Pygame community for their helpful documentation and tutorials.


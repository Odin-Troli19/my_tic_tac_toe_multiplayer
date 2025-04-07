# my_tic_tac_toe_multiplayer
A multiplayer Tic Tac Toe game with customizable player names and colors (red/blue). Features score tracking, game reset, and a clean interface. Play locally against a friend with automatic win detection and visual turn indicators.



# Tic Tac Toe Game

A multiplayer Tic Tac Toe game with customizable player names and colors. Play locally against a friend with score tracking and a clean interface.

## Features

- **Player Customization**: Enter player names and choose colors (red or blue)
- **Score Tracking**: Keeps track of wins for both players
- **Reset Options**: Reset the game board or clear scores completely
- **Visual Indicators**: Shows the current player's turn and highlights winning moves
- **Local Multiplayer**: Play on the same computer with a friend
- **Automatic Detection**: Game automatically detects wins and ties

## Requirements

- Python 3.x
- Tkinter (included in standard Python installation)

## How to Run


1. Run the game with the command:
   ```
   python tic_tac_toe.py
   ```

## Game Instructions

1. **Setup**:
   - Enter names for both players
   - Select colors (red or blue) for each player
   - Click "Start Game" when ready

2. **Gameplay**:
   - Players take turns clicking on empty cells to place their symbol (X or O)
   - The current player's turn is displayed above the game board
   - The game automatically determines when a player wins or when there's a tie

3. **Controls**:
   - "New Game": Clears the board while keeping the scores
   - "Reset Scores": Resets the scores to zero for both players

## Game Logic

The game checks for winning patterns:
- Three in a row horizontally
- Three in a row vertically
- Three in a row diagonally

If all cells are filled without a winner, the game declares a tie.

## Customization

You can modify the code to:
- Change colors
- Adjust the board size
- Add additional features like timed moves
- Implement an AI opponent for single-player mode

## License

This project is open source and available for personal and educational use.
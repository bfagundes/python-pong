# Classic Pong Game

A **classic Pong game** built in Python using the **turtle** library. This game supports both **single-player (with AI opponent)** and **two-player mode**. It features configurable difficulty levels, smooth ball physics, and a simple but effective AI opponent.

## Features

- **Single-player mode**: Play against an AI opponent with different difficulty levels.
- **Two-player mode**: Play locally with another player.
- **Configurable AI difficulty**:
  - **Easy**: Slow movement, delayed reactions, and frequent mistakes.
  - **Medium**: Moderate speed and accuracy.
  - **Hard**: Fast reactions, minimal mistakes.
- **Smooth Ball Physics**: Ball speed increases over time, bouncing angles adjust based on paddle impact.
- **Classic Pong-style scoring**: First to **7** points wins.
- **Simple UI**: White paddles and ball on a black background for an authentic retro feel.

## Screenshot
*(Add a screenshot of the game here)*

## Installation & Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/pong-game.git
   cd pong-game
   ```

2. **Install dependencies** (only required for `turtle`, which is included by default in Python):
   ```sh
   pip install turtle
   ```

3. **Run the game**:
   ```sh
   python main.py
   ```

## Controls

- **Player 1 (Left Paddle)**: `W` (up), `S` (down)
- **Player 2 (Right Paddle)**: `↑` (up), `↓` (down) *(Only active in two-player mode)*

### Activate Two-Player mode
To activate the two-player mode, set the `SINGLE_PLAYER` parameter on `config.py` to `False`

## ⚙️ Project Structure

```
pong_game/
│── main.py         # Runs the game  
│── ball.py         # Handles ball movement, speed, and collisions  
│── paddle.py       # Manages paddle movement and boundaries  
│── game.py         # Manages game logic (scoring, resets, AI, etc.)  
│── config.py       # Stores constants (speeds, colors, difficulty settings)  
│── plan.md         # Development plan and feature roadmap  
│── spec.md         # Game specifications and technical details  
```

## Future Improvements
- Add sound effects.
- Implement difficulty selection before the game starts.
- Improve AI logic for a more realistic challenge.
- Add a simple menu screen for mode selection.

## License
This project is open-source and available under the [MIT License](LICENSE).
# Snake

A classic Snake game built in Python with [pygame](https://www.pygame.org/).
Guide the snake to eat the food and grow as long as you can — without hitting
the walls or yourself.

## Features

- Smooth 60 FPS rendering with a separate, tunable movement speed
- Score counter
- Collision detection against walls and the snake's own body
- Automatic restart after a crash

## Controls

| Key | Action |
|-----|--------|
| `W` | Move up |
| `A` | Move left |
| `S` | Move down |
| `D` | Move right |
| `Esc` | Quit |

## Requirements

- Python 3.11+
- pygame

```bash
pip install pygame
```

## Run

```bash
python3 main.py
```

## Project structure

| File | Responsibility |
|------|----------------|
| `main.py` | Entry point — starts the game |
| `game.py` | Game state and the main loop |
| `snake.py` | The snake - movement, growth, collisions |
| `food.py` | The food the snake eats |
| `config.py` | Settings and constants |

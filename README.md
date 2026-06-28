# Knight Energy

A turn-based chess game between a human player and an AI, implemented with the **Minimax algorithm with alpha-beta pruning** and imperfect decisions.

## Game Rules

- 8×8 chess board.
- Each player controls a knight and starts with **7 energy units**.
- Each move costs **1 energy**.
- **Point squares** (values 2, 3, 4, 5, 6, 8, 9): gain points when landing on them.
- **Energy squares** (values 2, 3, 4, 5): recover energy when landing on them.
- No energy to move → skip turn and −3 points.
- Game ends when no point squares remain **or** neither player can move.
- The player with the most points wins.

## Difficulty Levels

| Level    | Minimax Depth |
|----------|---------------|
| Beginner | 2             |
| Amateur  | 4             |
| Expert   | 6             |

## Project Structure

```
proyecto2-IA/
├── main.py               # Entry point
├── requirements.txt
├── .gitignore
├── src/
│   ├── game/
│   │   ├── board.py      # Board and random placement
│   │   ├── knight.py     # Knight movement
│   │   ├── game_state.py # Game state
│   │   └── rules.py      # Rule validation
│   ├── ai/
│   │   ├── minimax.py    # Minimax algorithm with alpha-beta
│   │   └── heuristic.py  # Utility heuristic function
│   └── ui/
│       └── display.py    # Console display
├── tests/
│   ├── test_board.py
│   ├── test_minimax.py
│   └── test_game.py
└── docs/
    └── informe.md        # Heuristic function report
```

## Running

```bash
pip install -r requirements.txt
python main.py
```

## Team

| Member   | Main Responsibility                          |
|----------|----------------------------------------------|
| Member 1 | Game logic (board, rules, knights)           |
| Member 2 | AI: Minimax, heuristic, and report           |
| Member 3 | Game state, UI, integration, and testing     |

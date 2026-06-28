from src.game.board import (
    Board, EMPTY, POINT_CELL, ENERGY_CELL, WHITE_KNIGHT, BLACK_KNIGHT
)
from src.game.game_state import GameState

# Unicode symbols
SYM_WHITE = "♘"
SYM_BLACK = "♞"
SYM_POINT = "★"
SYM_ENERGY = "⚡"
SYM_EMPTY = "·"

COL_LABELS = "  a b c d e f g h"


def print_board(state: GameState) -> None:
    """Print the board and player stats to stdout."""
    board = state.board
    print()
    print(COL_LABELS)
    for row in range(Board.SIZE):
        row_str = f"{row + 1} "
        for col in range(Board.SIZE):
            pos = (row, col)
            cell = board.grid[row][col]
            if cell == WHITE_KNIGHT:
                row_str += SYM_WHITE + " "
            elif cell == BLACK_KNIGHT:
                row_str += SYM_BLACK + " "
            elif cell == POINT_CELL:
                value = board.point_map.get(pos, "?")
                row_str += f"{SYM_POINT}{value}"
            elif cell == ENERGY_CELL:
                value = board.energy_map.get(pos, "?")
                row_str += f"{SYM_ENERGY}{value}"
            else:
                row_str += SYM_EMPTY + " "
        print(row_str)
    print()
    _print_stats(state)


def _print_stats(state: GameState) -> None:
    """Print current points and energy for both players."""
    print(f"  Máquina  ({SYM_WHITE}) — Puntos: {state.white_points:3d}  Energía: {state.white_energy}")
    print(f"  Humano   ({SYM_BLACK}) — Puntos: {state.black_points:3d}  Energía: {state.black_energy}")
    print()


def print_winner(state: GameState) -> None:
    """Announce the result at the end of the game."""
    print("=" * 36)
    if state.winner == "white":
        print("  Gana la MÁQUINA. ¡Bien jugado, IA!")
    elif state.winner == "black":
        print("  Gana el HUMANO. ¡Felicitaciones!")
    else:
        print("  ¡EMPATE!")
    print(f"  Puntuación final — Máquina: {state.white_points}  Humano: {state.black_points}")
    print("=" * 36)


def ask_difficulty() -> str:
    """Prompt the user to select a difficulty level."""
    options = {"1": "principiante", "2": "amateur", "3": "experto"}
    print("Selecciona el nivel de dificultad:")
    print("  1 — Principiante (profundidad 2)")
    print("  2 — Amateur      (profundidad 4)")
    print("  3 — Experto      (profundidad 6)")
    while True:
        choice = input("Opción [1/2/3]: ").strip()
        if choice in options:
            return options[choice]
        print("Opción inválida. Intenta de nuevo.")


def ask_move(valid_moves: list[tuple]) -> tuple:
    """Prompt the human player to choose a move."""
    col_map = {c: i for i, c in enumerate("abcdefgh")}
    print("Movimientos disponibles:", [_pos_to_str(m) for m in valid_moves])
    while True:
        raw = input("Tu movimiento (ej: e5): ").strip().lower()
        if len(raw) == 2 and raw[0] in col_map and raw[1].isdigit():
            col = col_map[raw[0]]
            row = int(raw[1]) - 1
            dest = (row, col)
            if dest in valid_moves:
                return dest
        print("Movimiento inválido. Intenta de nuevo.")


def _pos_to_str(pos: tuple) -> str:
    col_label = "abcdefgh"[pos[1]]
    return f"{col_label}{pos[0] + 1}"

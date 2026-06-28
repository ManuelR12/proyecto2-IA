"""
Knight Energy — entry point.

Run with:
    python main.py
"""

from src.game.board import Board
from src.game.game_state import GameState
from src.game.rules import has_enough_energy
from src.game.knight import Knight
from src.ai.minimax import get_best_move
from src.ui.display import (
    print_board,
    print_winner,
    ask_difficulty,
    ask_move,
)


def main():
    print("=" * 36)
    print("       KNIGHT ENERGY")
    print("=" * 36)

    difficulty = ask_difficulty()
    state = GameState(Board())

    print(f"\nNivel: {difficulty.upper()}  — ¡Que empiece el juego!\n")
    print_board(state)

    while not state.game_over:
        if state.is_white_turn():
            _machine_turn(state, difficulty)
        else:
            _human_turn(state)

    print_board(state)
    print_winner(state)


def _machine_turn(state: GameState, difficulty: str) -> None:
    print("Turno de la MÁQUINA...")

    if not has_enough_energy(state.white_energy):
        print("La máquina no tiene energía. Pierde el turno (−3 puntos).")
        state.apply_skip_turn()
        return

    move = get_best_move(state, difficulty)
    if move is None:
        print("La máquina no tiene movimientos disponibles. Pierde el turno (−3 puntos).")
        state.apply_skip_turn()
        return

    col_label = "abcdefgh"[move[1]]
    print(f"La máquina mueve a {col_label}{move[0] + 1}")
    state.apply_move(move)
    print_board(state)


def _human_turn(state: GameState) -> None:
    print("Tu turno (HUMANO)...")

    if not has_enough_energy(state.black_energy):
        print("No tienes energía. Pierdes el turno (−3 puntos).")
        state.apply_skip_turn()
        return

    moves = state.available_moves()
    if not moves:
        print("No tienes movimientos disponibles. Pierdes el turno (−3 puntos).")
        state.apply_skip_turn()
        return

    destination = ask_move(moves)
    state.apply_move(destination)
    print_board(state)


if __name__ == "__main__":
    main()

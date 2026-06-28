from src.game.board import Board
from src.game.knight import Knight


def is_valid_move(pos: tuple, destination: tuple, board: Board) -> bool:
    """
    Returns True if moving a knight from `pos` to `destination` is a
    legal knight move within the board and not blocked by the other knight.
    """
    return destination in Knight.valid_moves(pos, board)


def has_enough_energy(energy: int) -> bool:
    """Returns True if the player has at least 1 energy to make a move."""
    return energy >= 1

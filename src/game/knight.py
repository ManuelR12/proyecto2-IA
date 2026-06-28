from src.game.board import Board

# All 8 possible L-shaped knight move deltas
KNIGHT_MOVES = [
    (-2, -1), (-2, 1),
    (-1, -2), (-1, 2),
    (1, -2),  (1, 2),
    (2, -1),  (2, 1),
]


class Knight:
    """Utility class for knight movement logic."""

    @staticmethod
    def valid_moves(pos: tuple, board: Board) -> list[tuple]:
        """
        Returns all valid destination squares for a knight at `pos`.

        A move is valid if:
        - The destination is within the 8x8 board.
        - The destination is not occupied by the other knight.
        """
        row, col = pos
        moves = []
        for dr, dc in KNIGHT_MOVES:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < Board.SIZE and 0 <= new_col < Board.SIZE:
                # Cannot land on the square occupied by the opposing knight
                if (new_row, new_col) != board.white_pos and (new_row, new_col) != board.black_pos:
                    moves.append((new_row, new_col))
        return moves

    @staticmethod
    def can_move(pos: tuple, board: Board) -> bool:
        """Returns True if the knight at `pos` has at least one valid move."""
        return len(Knight.valid_moves(pos, board)) > 0

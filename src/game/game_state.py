from src.game.board import Board
from src.game.knight import Knight

INITIAL_ENERGY = 7
SKIP_TURN_PENALTY = 3


class GameState:
    """
    Tracks the complete state of a Knight Energy game.

    Attributes:
        board (Board): Current board state.
        white_points (int): Points accumulated by the machine (white).
        black_points (int): Points accumulated by the human (black).
        white_energy (int): Remaining energy for the machine.
        black_energy (int): Remaining energy for the human.
        current_turn (str): 'white' or 'black' — whose turn it is.
        game_over (bool): True when the game has ended.
        winner (str | None): 'white', 'black', or 'draw' after game ends.
    """

    def __init__(self, board: Board = None):
        self.board = board if board is not None else Board()
        self.white_points: int = 0
        self.black_points: int = 0
        self.white_energy: int = INITIAL_ENERGY
        self.black_energy: int = INITIAL_ENERGY
        self.current_turn: str = "white"  # Machine always starts
        self.game_over: bool = False
        self.winner: str | None = None

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def is_white_turn(self) -> bool:
        return self.current_turn == "white"

    def current_energy(self) -> int:
        return self.white_energy if self.is_white_turn() else self.black_energy

    def current_pos(self) -> tuple:
        return self.board.white_pos if self.is_white_turn() else self.board.black_pos

    def available_moves(self) -> list[tuple]:
        """Returns the valid moves for the current player."""
        return Knight.valid_moves(self.current_pos(), self.board)

    # ------------------------------------------------------------------
    # Game progression
    # ------------------------------------------------------------------

    def apply_move(self, destination: tuple) -> None:
        """
        Apply a move for the current player.
        Deducts 1 energy, collects points/energy from the destination cell,
        then switches turns.
        """
        is_white = self.is_white_turn()

        # Deduct movement cost
        if is_white:
            self.white_energy -= 1
        else:
            self.black_energy -= 1

        points_gained, energy_gained = self.board.move_knight(is_white, destination)

        if is_white:
            self.white_points += points_gained
            self.white_energy += energy_gained
        else:
            self.black_points += points_gained
            self.black_energy += energy_gained

        self._switch_turn()
        self._check_game_over()

    def apply_skip_turn(self) -> None:
        """
        Penalise the current player for having no energy to move (−3 points),
        then switch turns.
        """
        if self.is_white_turn():
            self.white_points -= SKIP_TURN_PENALTY
        else:
            self.black_points -= SKIP_TURN_PENALTY
        self._switch_turn()

    def _switch_turn(self) -> None:
        self.current_turn = "black" if self.is_white_turn() else "white"

    def _check_game_over(self) -> None:
        """End the game if no point cells remain or neither player can move."""
        if not self.board.has_point_cells():
            self.game_over = True
        else:
            white_can = self.white_energy >= 1 and Knight.can_move(self.board.white_pos, self.board)
            black_can = self.black_energy >= 1 and Knight.can_move(self.board.black_pos, self.board)
            if not white_can and not black_can:
                self.game_over = True

        if self.game_over:
            self._determine_winner()

    def _determine_winner(self) -> None:
        if self.white_points > self.black_points:
            self.winner = "white"
        elif self.black_points > self.white_points:
            self.winner = "black"
        else:
            self.winner = "draw"

    # ------------------------------------------------------------------
    # Minimax helpers
    # ------------------------------------------------------------------

    def copy(self) -> "GameState":
        """Returns a deep copy suitable for minimax tree expansion."""
        new_state = GameState.__new__(GameState)
        new_state.board = self.board.copy()
        new_state.white_points = self.white_points
        new_state.black_points = self.black_points
        new_state.white_energy = self.white_energy
        new_state.black_energy = self.black_energy
        new_state.current_turn = self.current_turn
        new_state.game_over = self.game_over
        new_state.winner = self.winner
        return new_state

import random

# Board cell types
EMPTY = 0
POINT_CELL = 1
ENERGY_CELL = 2
WHITE_KNIGHT = 3  # Machine
BLACK_KNIGHT = 4  # Human

POINT_VALUES = [2, 3, 4, 5, 6, 8, 9]
ENERGY_VALUES = [2, 3, 4, 5]


class Board:
    """
    Represents the 8x8 chess board.

    Attributes:
        grid (list[list[int]]): Cell types on the board.
        point_map (dict[tuple, int]): Position -> point value for point cells.
        energy_map (dict[tuple, int]): Position -> energy value for energy cells.
        white_pos (tuple): Current position of the white knight (machine).
        black_pos (tuple): Current position of the black knight (human).
    """

    SIZE = 8

    def __init__(self):
        self.grid: list[list[int]] = [[EMPTY] * self.SIZE for _ in range(self.SIZE)]
        self.point_map: dict[tuple, int] = {}
        self.energy_map: dict[tuple, int] = {}
        self.white_pos: tuple = None
        self.black_pos: tuple = None
        self._place_pieces()

    def _random_free_cell(self, occupied: set) -> tuple:
        """Returns a random cell not in the occupied set."""
        while True:
            pos = (random.randint(0, self.SIZE - 1), random.randint(0, self.SIZE - 1))
            if pos not in occupied:
                return pos

    def _place_pieces(self):
        """Randomly place all pieces ensuring no overlaps."""
        occupied: set[tuple] = set()

        # Place white knight
        self.white_pos = self._random_free_cell(occupied)
        occupied.add(self.white_pos)
        self.grid[self.white_pos[0]][self.white_pos[1]] = WHITE_KNIGHT

        # Place black knight
        self.black_pos = self._random_free_cell(occupied)
        occupied.add(self.black_pos)
        self.grid[self.black_pos[0]][self.black_pos[1]] = BLACK_KNIGHT

        # Place point cells
        shuffled_points = POINT_VALUES[:]
        random.shuffle(shuffled_points)
        for value in shuffled_points:
            pos = self._random_free_cell(occupied)
            occupied.add(pos)
            self.grid[pos[0]][pos[1]] = POINT_CELL
            self.point_map[pos] = value

        # Place energy cells
        shuffled_energy = ENERGY_VALUES[:]
        random.shuffle(shuffled_energy)
        for value in shuffled_energy:
            pos = self._random_free_cell(occupied)
            occupied.add(pos)
            self.grid[pos[0]][pos[1]] = ENERGY_CELL
            self.energy_map[pos] = value

    def move_knight(self, is_white: bool, new_pos: tuple) -> tuple[int, int]:
        """
        Move a knight to new_pos and consume any cell there.

        Returns:
            (points_gained, energy_gained): Values collected (0 if none).
        """
        old_pos = self.white_pos if is_white else self.black_pos
        self.grid[old_pos[0]][old_pos[1]] = EMPTY

        points_gained = 0
        energy_gained = 0

        if new_pos in self.point_map:
            points_gained = self.point_map.pop(new_pos)
        elif new_pos in self.energy_map:
            energy_gained = self.energy_map.pop(new_pos)

        if is_white:
            self.white_pos = new_pos
        else:
            self.black_pos = new_pos

        self.grid[new_pos[0]][new_pos[1]] = WHITE_KNIGHT if is_white else BLACK_KNIGHT
        return points_gained, energy_gained

    def has_point_cells(self) -> bool:
        """Returns True if any point cell remains on the board."""
        return len(self.point_map) > 0

    def copy(self) -> "Board":
        """Returns a deep copy of this board (for minimax tree expansion)."""
        new_board = Board.__new__(Board)
        new_board.grid = [row[:] for row in self.grid]
        new_board.point_map = dict(self.point_map)
        new_board.energy_map = dict(self.energy_map)
        new_board.white_pos = self.white_pos
        new_board.black_pos = self.black_pos
        return new_board

"""Tests for Board and Knight movement logic — Persona 1."""

import pytest
from src.game.board import Board, POINT_VALUES, ENERGY_VALUES
from src.game.knight import Knight


class TestBoardInitialization:
    def test_board_size(self):
        board = Board()
        assert len(board.grid) == 8
        assert all(len(row) == 8 for row in board.grid)

    def test_point_cells_count(self):
        board = Board()
        assert len(board.point_map) == len(POINT_VALUES)

    def test_energy_cells_count(self):
        board = Board()
        assert len(board.energy_map) == len(ENERGY_VALUES)

    def test_point_values_correct(self):
        board = Board()
        assert sorted(board.point_map.values()) == sorted(POINT_VALUES)

    def test_energy_values_correct(self):
        board = Board()
        assert sorted(board.energy_map.values()) == sorted(ENERGY_VALUES)

    def test_no_overlapping_positions(self):
        board = Board()
        all_positions = (
            [board.white_pos, board.black_pos]
            + list(board.point_map.keys())
            + list(board.energy_map.keys())
        )
        assert len(all_positions) == len(set(all_positions)), "Positions overlap!"


class TestKnightMoves:
    def test_valid_moves_from_center(self):
        board = Board()
        # Manually place white at center; clear other pieces
        board.white_pos = (4, 4)
        board.black_pos = (0, 0)
        moves = Knight.valid_moves((4, 4), board)
        assert len(moves) == 8

    def test_valid_moves_from_corner(self):
        board = Board()
        board.white_pos = (0, 0)
        board.black_pos = (7, 7)
        moves = Knight.valid_moves((0, 0), board)
        assert len(moves) == 2  # Only (1,2) and (2,1)

    def test_cannot_land_on_other_knight(self):
        board = Board()
        board.white_pos = (0, 0)
        board.black_pos = (1, 2)  # Reachable from (0,0)
        moves = Knight.valid_moves((0, 0), board)
        assert (1, 2) not in moves

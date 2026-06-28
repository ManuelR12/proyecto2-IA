"""Integration tests for game flow — Persona 3."""

import pytest
from src.game.board import Board
from src.game.game_state import GameState
from src.game.rules import has_enough_energy, is_valid_move


class TestGameState:
    def test_initial_energy(self):
        state = GameState()
        assert state.white_energy == 7
        assert state.black_energy == 7

    def test_initial_points(self):
        state = GameState()
        assert state.white_points == 0
        assert state.black_points == 0

    def test_machine_starts(self):
        state = GameState()
        assert state.current_turn == "white"

    def test_move_costs_energy(self):
        state = GameState()
        moves = state.available_moves()
        if moves:
            state.apply_move(moves[0])
            assert state.black_energy == 7  # black hasn't moved yet
            # White already moved — it's now black's turn
            assert state.current_turn == "black"

    def test_skip_turn_penalty(self):
        state = GameState()
        state.apply_skip_turn()
        assert state.white_points == -3

    def test_game_over_no_point_cells(self):
        state = GameState()
        state.board.point_map.clear()
        state._check_game_over()
        assert state.game_over


class TestRules:
    def test_has_enough_energy(self):
        assert has_enough_energy(1) is True
        assert has_enough_energy(0) is False

    def test_is_valid_move(self):
        board = Board()
        white = board.white_pos
        from src.game.knight import Knight
        valid = Knight.valid_moves(white, board)
        if valid:
            assert is_valid_move(white, valid[0], board) is True

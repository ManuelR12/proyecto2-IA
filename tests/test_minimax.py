"""Tests for Minimax and heuristic — Persona 2."""

import pytest
from src.game.board import Board
from src.game.game_state import GameState
from src.ai.heuristic import evaluate
from src.ai.minimax import get_best_move


class TestHeuristic:
    def test_terminal_white_wins(self):
        state = GameState()
        state.game_over = True
        state.winner = "white"
        assert evaluate(state) == float("inf")

    def test_terminal_black_wins(self):
        state = GameState()
        state.game_over = True
        state.winner = "black"
        assert evaluate(state) == float("-inf")

    def test_terminal_draw(self):
        state = GameState()
        state.game_over = True
        state.winner = "draw"
        assert evaluate(state) == 0.0

    def test_higher_points_positive(self):
        state = GameState()
        state.white_points = 10
        state.black_points = 0
        assert evaluate(state) > 0


class TestMinimax:
    def test_returns_valid_move(self):
        state = GameState()
        move = get_best_move(state, "principiante")
        assert move is not None
        assert move in state.available_moves()

    def test_no_move_when_no_energy(self):
        state = GameState()
        state.white_energy = 0
        move = get_best_move(state, "principiante")
        assert move is None

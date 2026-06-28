import math
from src.game.game_state import GameState
from src.game.knight import Knight, KNIGHT_MOVES

# Weights for the heuristic components (tune during development)
W_POINTS = 1.0       # Score difference
W_ENERGY = 0.5       # Energy difference
W_MOBILITY = 0.3     # Mobility difference (available moves)
W_PROXIMITY = 0.4    # Proximity to high-value point cells


def evaluate(state: GameState) -> float:
    """
    Heuristic utility function for Minimax.

    Positive values favour the machine (white); negative values favour the human (black).

    Components:
    1. **Point difference**   — white_points − black_points, weighted by W_POINTS.
    2. **Energy difference**  — white_energy − black_energy, weighted by W_ENERGY.
    3. **Mobility difference**— (white available moves) − (black available moves),
                                weighted by W_MOBILITY.
    4. **Proximity bonus**    — for white: how close it is to the highest remaining
                                point cell; penalised for black proximity as well.
    """
    if state.game_over:
        if state.winner == "white":
            return float("inf")
        if state.winner == "black":
            return float("-inf")
        return 0.0

    score = 0.0

    # 1. Point difference
    score += W_POINTS * (state.white_points - state.black_points)

    # 2. Energy difference
    score += W_ENERGY * (state.white_energy - state.black_energy)

    # 3. Mobility difference
    white_moves = len(Knight.valid_moves(state.board.white_pos, state.board))
    black_moves = len(Knight.valid_moves(state.board.black_pos, state.board))
    score += W_MOBILITY * (white_moves - black_moves)

    # 4. Proximity to highest-value point cell
    if state.board.point_map:
        best_value = max(state.board.point_map.values())
        best_pos = [p for p, v in state.board.point_map.items() if v == best_value][0]

        white_dist = _chebyshev_distance(state.board.white_pos, best_pos)
        black_dist = _chebyshev_distance(state.board.black_pos, best_pos)

        # Closer white → better; closer black → worse for white
        proximity_score = (black_dist - white_dist) * best_value * 0.1
        score += W_PROXIMITY * proximity_score

    return score


def _chebyshev_distance(a: tuple, b: tuple) -> int:
    """
    Chebyshev distance between two board squares — approximates knight
    reachability without expensive BFS.
    """
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

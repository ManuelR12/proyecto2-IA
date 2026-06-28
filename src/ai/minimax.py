from src.game.game_state import GameState
from src.game.knight import Knight
from src.ai.heuristic import evaluate

DIFFICULTY_DEPTH = {
    "principiante": 2,
    "amateur": 4,
    "experto": 6,
}


def get_best_move(state: GameState, difficulty: str) -> tuple | None:
    """
    Returns the best destination square for the current player (white/machine)
    using Minimax with alpha-beta pruning.

    Args:
        state:      Current game state.
        difficulty: One of 'principiante', 'amateur', 'experto'.

    Returns:
        The best destination tuple, or None if no move is available.
    """
    depth = DIFFICULTY_DEPTH.get(difficulty, 2)
    moves = state.available_moves()
    if not moves:
        return None

    best_value = float("-inf")
    best_move = None

    for move in moves:
        child = state.copy()
        child.apply_move(move)
        value = _minimax(child, depth - 1, float("-inf"), float("inf"), is_maximizing=False)
        if value > best_value:
            best_value = value
            best_move = move

    return best_move


def _minimax(state: GameState, depth: int, alpha: float, beta: float, is_maximizing: bool) -> float:
    """
    Recursive Minimax with alpha-beta pruning.

    White (machine) is the maximising player.
    Black (human)   is the minimising player.
    """
    if depth == 0 or state.game_over:
        return evaluate(state)

    moves = state.available_moves()

    # No energy or no valid moves → forced skip
    if not moves or state.current_energy() < 1:
        child = state.copy()
        child.apply_skip_turn()
        return _minimax(child, depth - 1, alpha, beta, not is_maximizing)

    if is_maximizing:
        max_eval = float("-inf")
        for move in moves:
            child = state.copy()
            child.apply_move(move)
            eval_score = _minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = float("inf")
        for move in moves:
            child = state.copy()
            child.apply_move(move)
            eval_score = _minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

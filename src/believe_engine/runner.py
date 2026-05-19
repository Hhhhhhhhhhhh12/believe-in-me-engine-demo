from __future__ import annotations

from dataclasses import dataclass

from .legal_moves import LegalMove, legal_moves
from .rng import SeededRng
from .rules import apply_move, build_sample_deck, create_game
from .state import GameState


@dataclass(frozen=True, slots=True)
class RunResult:
    seed: int
    final_state: GameState
    turn_count: int

    @property
    def winner_id(self) -> str | None:
        return self.final_state.winner_id


def run_match(*, seed: int, player_count: int = 3, max_turns: int = 60) -> RunResult:
    rng = SeededRng(seed)
    deck = rng.shuffled(build_sample_deck())
    state = create_game(player_count=player_count, deck=deck)

    turn_count = 0
    while not state.is_finished and turn_count < max_turns:
        move = choose_demo_move(state, rng=rng)
        state = apply_move(state, move)
        turn_count += 1

    return RunResult(seed=seed, final_state=state, turn_count=turn_count)


def choose_demo_move(state: GameState, *, rng: SeededRng) -> LegalMove:
    moves = legal_moves(state)
    winning_cards = [
        move
        for move in moves
        if move.action == "play_card"
        and _projected_progress(state, move) >= state.target_progress
    ]
    if winning_cards:
        return winning_cards[0]

    convert_moves = [move for move in moves if move.action == "convert"]
    if convert_moves and state.active_player.progress >= state.target_progress - 2:
        return convert_moves[0]

    playable_cards = [move for move in moves if move.action == "play_card"]
    if playable_cards:
        return max(playable_cards, key=lambda move: _projected_progress(state, move))

    if convert_moves:
        return convert_moves[0]

    gather_moves = [move for move in moves if move.action == "gather"]
    if gather_moves:
        return gather_moves[0]

    return rng.choice(moves)


def _projected_progress(state: GameState, move: LegalMove) -> int:
    player = state.active_player
    if move.action == "convert":
        return player.progress + 2
    if move.action == "play_card":
        for card in player.hand:
            if card.card_id == move.card_id:
                return player.progress + card.progress
    return player.progress

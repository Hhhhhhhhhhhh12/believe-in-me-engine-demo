from dataclasses import replace

from portfolio_engine.legal_moves import legal_moves
from portfolio_engine.rules import create_game
from portfolio_engine.state import replace_player


def test_gather_and_pass_are_always_available_during_match() -> None:
    state = create_game(player_count=3)

    assert {move.action for move in legal_moves(state)} >= {"gather", "pass"}


def test_convert_requires_three_resources() -> None:
    state = create_game(player_count=3)
    assert "convert" not in {move.action for move in legal_moves(state)}

    player = replace(state.active_player, resources=3)
    state = replace_player(state, player)

    assert "convert" in {move.action for move in legal_moves(state)}


def test_play_card_requires_enough_resources() -> None:
    state = create_game(player_count=3)
    player = state.active_player
    expensive_card = replace(player.hand[0], cost=99)
    state = replace_player(state, replace(player, hand=(expensive_card,)))

    assert "play_card" not in {move.action for move in legal_moves(state)}

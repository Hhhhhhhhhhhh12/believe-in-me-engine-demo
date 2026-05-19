from __future__ import annotations

from dataclasses import replace

from .legal_moves import LegalMove, legal_moves
from .state import DemoCard, GameState, PlayerState, replace_player


def build_sample_deck() -> tuple[DemoCard, ...]:
    return (
        DemoCard("card-advance-1", "Advance", cost=2, progress=2),
        DemoCard("card-advance-2", "Advance", cost=2, progress=2),
        DemoCard("card-boost-1", "Boost", cost=3, progress=4),
        DemoCard("card-boost-2", "Boost", cost=3, progress=4),
        DemoCard("card-focus-1", "Focus", cost=1, progress=1),
        DemoCard("card-focus-2", "Focus", cost=1, progress=1),
        DemoCard("card-sprint-1", "Sprint", cost=4, progress=5),
        DemoCard("card-sprint-2", "Sprint", cost=4, progress=5),
    )


def create_game(*, player_count: int = 3, deck: tuple[DemoCard, ...] | None = None) -> GameState:
    if player_count < 2:
        raise ValueError("At least two players are required.")

    draw_pile = deck or build_sample_deck()
    players = tuple(
        PlayerState(player_id=f"p{index + 1}", hand=draw_pile[index : index + 1])
        for index in range(player_count)
    )
    return GameState(players=players, draw_pile=draw_pile[player_count:])


def apply_move(state: GameState, move: LegalMove) -> GameState:
    if move not in legal_moves(state):
        raise ValueError(f"Illegal move for {state.active_player.player_id}: {move}.")

    player = state.active_player
    next_state = state

    if move.action == "gather":
        next_state = replace_player(state, replace(player, resources=player.resources + 1))
        next_state = _append_event(next_state, "resource_gained", amount=1)
    elif move.action == "convert":
        updated = replace(player, resources=player.resources - 3, progress=player.progress + 2)
        next_state = replace_player(state, updated)
        next_state = _append_event(next_state, "resources_converted", cost=3, progress=2)
    elif move.action == "play_card":
        card = _find_card(player, move.card_id)
        remaining_hand = tuple(current for current in player.hand if current.card_id != card.card_id)
        updated = replace(
            player,
            resources=player.resources - card.cost,
            progress=player.progress + card.progress,
            hand=remaining_hand,
            discard_count=player.discard_count + 1,
        )
        next_state = replace_player(state, updated)
        next_state = _append_event(
            next_state,
            "card_played",
            card_id=card.card_id,
            card_name=card.name,
            cost=card.cost,
            progress=card.progress,
        )
    elif move.action == "pass":
        next_state = _append_event(state, "turn_passed")

    next_state = _check_winner(next_state)
    if next_state.is_finished:
        return next_state
    return _advance_turn(next_state)


def _find_card(player: PlayerState, card_id: str | None) -> DemoCard:
    for card in player.hand:
        if card.card_id == card_id:
            return card
    raise ValueError(f"Card is not in hand: {card_id}.")


def _advance_turn(state: GameState) -> GameState:
    next_turn_index = (state.turn_index + 1) % len(state.players)
    next_round = state.round_number + 1 if next_turn_index == 0 else state.round_number
    return replace(state, turn_index=next_turn_index, round_number=next_round)


def _check_winner(state: GameState) -> GameState:
    for player in state.players:
        if player.progress >= state.target_progress:
            return _append_event(replace(state, winner_id=player.player_id), "match_finished", winner_id=player.player_id)
    return state


def _append_event(state: GameState, event_type: str, **payload: object) -> GameState:
    event = {
        "round": state.round_number,
        "turn_index": state.turn_index,
        "player_id": state.active_player.player_id,
        "type": event_type,
        **payload,
    }
    return replace(state, events=(*state.events, event))

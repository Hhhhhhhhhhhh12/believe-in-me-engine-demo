from __future__ import annotations

from dataclasses import dataclass

from .state import ActionType, GameState


@dataclass(frozen=True, slots=True)
class LegalMove:
    action: ActionType
    card_id: str | None = None
    reason: str = ""


def legal_moves(state: GameState) -> tuple[LegalMove, ...]:
    if state.is_finished:
        return ()

    player = state.active_player
    moves: list[LegalMove] = [
        LegalMove("gather", reason="Gain one generic resource."),
        LegalMove("pass", reason="End the current player's turn."),
    ]

    if player.resources >= 3:
        moves.append(LegalMove("convert", reason="Convert three resources into two progress."))

    for card in player.hand:
        if player.resources >= card.cost:
            moves.append(
                LegalMove(
                    "play_card",
                    card_id=card.card_id,
                    reason=f"Spend {card.cost} resources for {card.progress} progress.",
                )
            )

    return tuple(moves)

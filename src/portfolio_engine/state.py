from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Literal


ActionType = Literal["gather", "play_card", "convert", "pass"]


@dataclass(frozen=True, slots=True)
class DemoCard:
    card_id: str
    name: str
    cost: int
    progress: int


@dataclass(frozen=True, slots=True)
class PlayerState:
    player_id: str
    resources: int = 1
    progress: int = 0
    hand: tuple[DemoCard, ...] = ()
    discard_count: int = 0


@dataclass(frozen=True, slots=True)
class GameState:
    players: tuple[PlayerState, ...]
    draw_pile: tuple[DemoCard, ...]
    turn_index: int = 0
    round_number: int = 1
    target_progress: int = 10
    winner_id: str | None = None
    events: tuple[dict[str, object], ...] = field(default_factory=tuple)

    @property
    def active_player(self) -> PlayerState:
        return self.players[self.turn_index % len(self.players)]

    @property
    def is_finished(self) -> bool:
        return self.winner_id is not None


def replace_player(state: GameState, player: PlayerState) -> GameState:
    players = tuple(player if current.player_id == player.player_id else current for current in state.players)
    return replace(state, players=players)

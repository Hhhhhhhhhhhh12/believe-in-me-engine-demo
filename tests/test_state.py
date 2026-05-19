from believe_engine.rules import create_game


def test_create_game_deals_one_card_per_player() -> None:
    state = create_game(player_count=3)

    assert [player.player_id for player in state.players] == ["p1", "p2", "p3"]
    assert all(len(player.hand) == 1 for player in state.players)
    assert state.active_player.player_id == "p1"
    assert not state.is_finished


def test_target_progress_uses_sample_value() -> None:
    state = create_game(player_count=2)

    assert state.target_progress == 10

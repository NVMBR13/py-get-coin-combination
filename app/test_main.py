import pytest


from app.main import get_coin_combination


@pytest.mark.parametrize(
    "coins, result",
    [(1, [1, 0, 0, 0]),
     (6, [1, 1, 0, 0]),
     (17, [2, 1, 1, 0]),
     (50, [0, 0, 0, 2])],
)
def test_coin_combination(coins: int, result: list[int]) -> None:
    assert get_coin_combination(coins) == result

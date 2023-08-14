import pytest
from solutions.sol_1140 import Solution

cases = [
    {"input": {"piles": [2, 7, 9, 4, 4]}, "output": 10},
    {"input": {"piles": [1, 2, 3, 4, 5, 100]}, "output": 104},
]


@pytest.mark.sol1140
def test_run():
    for case in cases:
        assert Solution.stone_game_2(piles=case["input"]["piles"]) == case["output"]

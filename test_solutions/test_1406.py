import pytest
from solutions.sol_1406 import Solution

cases = [
    {
        "input": {
            "stone_value": [1, 2, 3, 7],
        },
        "output": "Bob",
    },
    {
        "input": {
            "stone_value": [1, 2, 3, -9],
        },
        "output": "Alice",
    },
    {
        "input": {
            "stone_value": [1, 2, 3, 6],
        },
        "output": "Tie",
    },
    {
        "input": {
            "stone_value": [-1, -2, -3],
        },
        "output": "Tie",
    },
]


@pytest.mark.sol1406
def test_run():
    for case in cases:
        assert (
            Solution.stone_game_3(stone_value=case["input"]["stone_value"])
            == case["output"]
        )

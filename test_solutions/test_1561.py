import pytest
from solutions.sol_1561 import Solution

cases = [
    {
        "input": {
            "piles": [2, 4, 1, 2, 7, 8],
        },
        "output": 9,
    },
    {
        "input": {
            "piles": [2, 4, 5],
        },
        "output": 4,
    },
    {
        "input": {
            "piles": [9, 8, 7, 6, 5, 1, 2, 3, 4],
        },
        "output": 18,
    },
]


@pytest.mark.sol1561
def test_run():
    for case in cases:
        assert (
            Solution.max_coins(
                piles=case["input"]["piles"],
            )
            == case["output"]
        )

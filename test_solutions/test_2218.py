import pytest
from solutions.sol_2218 import Solution

cases = [
    {
        "input": {
            "piles": [[1, 100, 3], [7, 8, 9]],
            "k": 2,
        },
        "output": 101,
    },
    {
        "input": {
            "piles": [
                [100],
                [100],
                [100],
                [100],
                [100],
                [100],
                [1, 1, 1, 1, 1, 1, 700],
            ],
            "k": 7,
        },
        "output": 706,
    },
]


@pytest.mark.sol_2218
def test_run():
    for case in cases:
        assert (
            Solution.max_value_of_coins(
                piles=case["input"]["piles"],
                k=case["input"]["k"],
            )
            == case["output"]
        )

import pytest
from solutions.sol_1463 import Solution

cases = [
    {
        "input": {
            "grid": [[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]],
        },
        "output": 24,
    },
    {
        "input": {
            "grid": [
                [1, 0, 0, 0, 0, 0, 1],
                [2, 0, 0, 0, 0, 3, 0],
                [2, 0, 9, 0, 0, 0, 0],
                [0, 3, 0, 5, 4, 0, 0],
                [1, 0, 2, 3, 0, 0, 6],
            ],
        },
        "output": 28,
    },
]


@pytest.mark.sol1463
def test_run():
    for case in cases:
        assert (
            Solution.cherry_pickup(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )

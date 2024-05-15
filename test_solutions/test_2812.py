import pytest
from solutions.sol_2812 import Solution

cases = [
    {
        "input": {
            "grid": [[1, 0, 0], [0, 0, 0], [0, 0, 1]],
        },
        "output": 0,
    },
    {
        "input": {
            "grid": [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
        },
        "output": 2,
    },
    {
        "input": {
            "grid": [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]],
        },
        "output": 2,
    },
    {
        "input": {
            "grid": [[1, 1, 1], [0, 1, 1], [0, 0, 0]],
        },
        "output": 0,
    },
]


@pytest.mark.sol_2812
def test_run():
    for case in cases:
        assert (
            Solution.maximum_safeness_factor(grid=case["input"]["grid"])
            == case["output"]
        )

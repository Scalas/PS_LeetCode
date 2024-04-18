import pytest
from solutions.sol_463 import Solution

cases = [
    {
        "input": {
            "grid": [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],
        },
        "output": 16,
    },
    {
        "input": {
            "grid": [[1]],
        },
        "output": 4,
    },
    {
        "input": {
            "grid": [[1, 0]],
        },
        "output": 4,
    },
]


@pytest.mark.sol_463
def test_run():
    for case in cases:
        assert Solution.island_perimeter(grid=case["input"]["grid"]) == case["output"]

import pytest
from solutions.sol_1162 import Solution

cases = [
    {
        "input": {
            "grid": [[1, 0, 1], [0, 0, 0], [1, 0, 1]],
        },
        "output": 2,
    },
    {
        "input": {
            "grid": [[1, 0, 0], [0, 0, 0], [0, 0, 0]],
        },
        "output": 4,
    },
]


@pytest.mark.sol1162
def test_run():
    for case in cases:
        assert (
            Solution.max_distance(
                grid=case["input"]["grid"],
            )
            == case["output"]
        )

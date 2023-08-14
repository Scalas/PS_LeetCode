import pytest
from solutions.sol_1466 import Solution

cases = [
    {
        "input": {
            "n": 6,
            "connections": [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]],
        },
        "output": 3,
    },
    {
        "input": {
            "n": 5,
            "connections": [[1, 0], [1, 2], [3, 2], [3, 4]],
        },
        "output": 2,
    },
    {
        "input": {
            "n": 3,
            "connections": [[1, 0], [2, 0]],
        },
        "output": 0,
    },
]


@pytest.mark.sol1466
def test_run():
    for case in cases:
        assert (
            Solution.min_reorder(
                n=case["input"]["n"],
                connections=case["input"]["connections"],
            )
            == case["output"]
        )

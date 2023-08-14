import pytest
from solutions.sol_934 import Solution

cases = [
    {
        "input": {
            "grid": [[0, 1], [1, 0]],
        },
        "output": 1,
    },
    {
        "input": {
            "grid": [[0, 1, 0], [0, 0, 0], [0, 0, 1]],
        },
        "output": 2,
    },
    {
        "input": {
            "grid": [
                [1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1],
            ],
        },
        "output": 1,
    },
]


@pytest.mark.sol934
def test_run():
    for case in cases:
        assert Solution.shortest_bridge(grid=case["input"]["grid"]) == case["output"]

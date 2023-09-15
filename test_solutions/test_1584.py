import pytest
from solutions.sol_1584 import Solution

cases = [
    {
        "input": {
            "points": [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]],
        },
        "output": 20,
    },
    {
        "input": {
            "points": [[3, 12], [-2, 5], [-4, 1]],
        },
        "output": 18,
    },
    {
        "input": {
            "points": [[1, 1]],
        },
        "output": 0,
    },
]


@pytest.mark.sol1584
def test_run():
    for case in cases:
        assert (
            Solution.min_cost_connect_points(
                points=case["input"]["points"],
            )
            == case["output"]
        )

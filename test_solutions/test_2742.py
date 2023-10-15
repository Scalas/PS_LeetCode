import pytest
from solutions.sol_2742 import Solution

cases = [
    {
        "input": {
            "cost": [1, 2, 3, 2],
            "time": [1, 2, 3, 2],
        },
        "output": 3,
    },
    {
        "input": {
            "cost": [2, 3, 4, 2],
            "time": [1, 1, 1, 1],
        },
        "output": 4,
    },
]


@pytest.mark.sol_2742
def test_run():
    for case in cases:
        assert (
            Solution.paint_walls(cost=case["input"]["cost"], time=case["input"]["time"])
            == case["output"]
        )

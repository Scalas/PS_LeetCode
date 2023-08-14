import pytest
from solutions.sol_2448 import Solution

cases = [
    {
        "input": {
            "nums": [1, 3, 5, 2],
            "cost": [2, 3, 1, 14],
        },
        "output": 8,
    },
    {
        "input": {
            "nums": [2, 2, 2, 2, 2],
            "cost": [4, 2, 8, 1, 3],
        },
        "output": 0,
    },
    {
        "input": {
            "nums": [1, 7, 2, 8, 3, 5, 4, 3],
            "cost": [3, 1, 300, 2, 500, 10000, 400, 600],
        },
        "output": 3520,
    },
]


@pytest.mark.sol_2448
def test_run():
    for case in cases:
        assert (
            Solution.min_cost(nums=case["input"]["nums"], cost=case["input"]["cost"])
            == case["output"]
        )

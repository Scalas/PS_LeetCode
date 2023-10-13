import pytest
from solutions.sol_746 import Solution

cases = [
    {"input": {"cost": [10, 15, 20]}, "output": 15},
    {"input": {"cost": [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]}, "output": 6},
]


@pytest.mark.sol_746
def test_run():
    for case in cases:
        assert (
            Solution.min_cost_climbing_stairs(
                cost=case["input"]["cost"],
            )
            == case["output"]
        )

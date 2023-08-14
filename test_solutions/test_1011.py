import pytest
from solutions.sol_1011 import Solution

cases = [
    {"input": {"weights": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "days": 5}, "output": 15},
    {"input": {"weights": [3, 2, 2, 4, 1, 4], "days": 3}, "output": 6},
    {"input": {"weights": [1, 2, 3, 1, 1], "days": 4}, "output": 3},
]


@pytest.mark.sol1011
def test_run():
    for case in cases:
        assert (
            Solution.ship_within_days(
                weights=case["input"]["weights"], days=case["input"]["days"]
            )
            == case["output"]
        )

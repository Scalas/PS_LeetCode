import pytest
from solutions.sol_1523 import Solution

cases = [
    {
        "input": {
            "low": 3,
            "high": 7,
        },
        "output": 3,
    },
    {
        "input": {
            "low": 8,
            "high": 10,
        },
        "output": 1,
    },
]


@pytest.mark.sol1523
def test_run():
    for case in cases:
        assert (
            Solution.count_odds(
                low=case["input"]["low"],
                high=case["input"]["high"],
            )
            == case["output"]
        )

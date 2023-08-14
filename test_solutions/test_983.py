import pytest
from solutions.sol_983 import Solution

cases = [
    {
        "input": {
            "days": [1, 4, 6, 7, 8, 20],
            "costs": [2, 7, 15],
        },
        "output": 11,
    },
    {
        "input": {
            "days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31],
            "costs": [2, 7, 15],
        },
        "output": 17,
    },
]


@pytest.mark.sol983
def test_run():
    for case in cases:
        assert (
            Solution.min_cost_tickets(
                days=case["input"]["days"],
                costs=case["input"]["costs"],
            )
            == case["output"]
        )

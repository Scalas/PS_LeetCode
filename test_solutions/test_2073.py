import pytest
from solutions.sol_2073 import Solution

cases = [
    {
        "input": {
            "tickets": [2, 3, 2],
            "k": 2,
        },
        "output": 6,
    },
    {
        "input": {
            "tickets": [5, 1, 1, 1],
            "k": 0,
        },
        "output": 8,
    },
]


@pytest.mark.sol_2073
def test_run():
    for case in cases:
        assert (
            Solution.time_required_to_buy(
                tickets=case["input"]["tickets"],
                k=case["input"]["k"],
            )
            == case["output"]
        )

import pytest
from solutions.sol_1701 import Solution


cases = [
    {
        "input": {
            "customers": [[1, 2], [2, 5], [4, 3]]
        },
        "output": 5.00000,
    },
    {
        "input": {
            "customers": [[5, 2], [5, 4], [10, 3], [20, 1]]
        },
        "output": 3.25000,
    },
]


@pytest.mark.sol1701
def test_run():
    for case in cases:
        assert (
            Solution.average_waiting_time(
                customers=case["input"]["customers"],
            )
            == case["output"]
        )

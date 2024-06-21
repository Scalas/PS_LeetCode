import pytest
from solutions.sol_1052 import Solution

cases = [
    {
        "input": {
            "customers": [1, 0, 1, 2, 1, 1, 7, 5],
            "grumpy": [0, 1, 0, 1, 0, 1, 0, 1],
            "minutes": 3,
        },
        "output": 16,
    },
    {
        "input": {
            "customers": [1],
            "grumpy": [0],
            "minutes": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "customers": [10, 1, 7],
            "grumpy": [0, 0, 0],
            "minutes": 2,
        },
        "output": 18,
    },
]


@pytest.mark.sol1052
def test_run():
    for case in cases:
        assert (
            Solution.max_satisfied(
                customers=case["input"]["customers"],
                grumpy=case["input"]["grumpy"],
                minutes=case["input"]["minutes"],
            )
            == case["output"]
        )

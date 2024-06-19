import pytest
from solutions.sol_1482 import Solution

cases = [
    {
        "input": {
            "bloom_day": [1, 10, 3, 10, 2],
            "m": 3,
            "k": 1,
        },
        "output": 3,
    },
    {
        "input": {
            "bloom_day": [1, 10, 3, 10, 2],
            "m": 3,
            "k": 2,
        },
        "output": -1,
    },
    {
        "input": {
            "bloom_day": [7, 7, 7, 7, 12, 7, 7],
            "m": 2,
            "k": 3,
        },
        "output": 12,
    },
]


@pytest.mark.sol1482
def test_run():
    for case in cases:
        assert (
            Solution.min_days(
                bloom_day=case["input"]["bloom_day"],
                m=case["input"]["m"],
                k=case["input"]["k"],
            )
            == case["output"]
        )

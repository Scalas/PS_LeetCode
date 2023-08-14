import pytest
from solutions.sol_1802 import Solution

cases = [
    {
        "input": {
            "n": 4,
            "index": 2,
            "max_sum": 6,
        },
        "output": 2,
    },
    {
        "input": {
            "n": 6,
            "index": 1,
            "max_sum": 10,
        },
        "output": 3,
    },
    {
        "input": {
            "n": 2,
            "index": 1,
            "max_sum": 21,
        },
        "output": 11,
    },
]


@pytest.mark.sol1802
def test_run():
    for case in cases:
        assert (
            Solution.max_value(
                n=case["input"]["n"],
                index=case["input"]["index"],
                max_sum=case["input"]["max_sum"],
            )
            == case["output"]
        )

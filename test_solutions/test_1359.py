import pytest

from solutions.sol_1359 import Solution

cases = [
    {
        "input": {
            "n": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "n": 2,
        },
        "output": 6,
    },
    {
        "input": {
            "n": 3,
        },
        "output": 90,
    },
]


@pytest.mark.sol1359
def test_run():
    for case in cases:
        assert (
            Solution.count_orders(
                n=case["input"]["n"],
            )
            == case["output"]
        )

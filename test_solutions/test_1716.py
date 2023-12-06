import pytest
from solutions.sol_1716 import Solution

cases = [
    {
        "input": {
            "n": 4,
        },
        "output": 10,
    },
    {
        "input": {
            "n": 10,
        },
        "output": 37,
    },
    {
        "input": {
            "n": 20,
        },
        "output": 96,
    },
]


@pytest.mark.sol1716
def test_run():
    for case in cases:
        assert (
            Solution.total_money(
                n=case["input"]["n"],
            )
            == case["output"]
        )

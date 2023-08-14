import pytest
from solutions.sol_50 import Solution

cases = [
    {
        "input": {
            "x": 2.00000,
            "n": 10,
        },
        "output": 1024.00000,
    },
    {
        "input": {
            "x": 2.10000,
            "n": 3,
        },
        "output": 9.26100,
    },
    {
        "input": {
            "x": 2.00000,
            "n": -2,
        },
        "output": 0.25000,
    },
]


@pytest.mark.sol50
def test_run():
    for case in cases:
        assert (
            round(
                Solution.my_pow(
                    x=case["input"]["x"],
                    n=case["input"]["n"],
                ),
                5,
            )
            == case["output"]
        )

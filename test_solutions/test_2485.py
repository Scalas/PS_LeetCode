import pytest
from solutions.sol_2485 import Solution

cases = [
    {
        "input": {
            "n": 8,
        },
        "output": 6,
    },
    {
        "input": {
            "n": 1,
        },
        "output": 1,
    },
    {
        "input": {
            "n": 4,
        },
        "output": -1,
    },
]


@pytest.mark.sol_2485
def test_run():
    for case in cases:
        assert (
            Solution.pivot_integer(
                n=case["input"]["n"],
            )
            == case["output"]
        )

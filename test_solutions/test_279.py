import pytest
from solutions.sol_279 import Solution

cases = [
    {
        "input": {
            "n": 12,
        },
        "output": 3,
    },
    {
        "input": {
            "n": 13,
        },
        "output": 2,
    },
]


@pytest.mark.sol279
def test_run():
    for case in cases:
        assert (
            Solution.num_squares(
                n=case["input"]["n"],
            )
            == case["output"]
        )

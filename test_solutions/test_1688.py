import pytest
from solutions.sol_1688 import Solution

cases = [
    {
        "input": {
            "n": 7,
        },
        "output": 6,
    },
    {
        "input": {
            "n": 14,
        },
        "output": 13,
    },
]


@pytest.mark.sol1688
def test_run():
    for case in cases:
        assert (
            Solution.number_of_matches(
                n=case["input"]["n"],
            )
            == case["output"]
        )

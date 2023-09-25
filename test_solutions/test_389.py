import pytest
from solutions.sol_389 import Solution

cases = [
    {
        "input": {
            "s": "abcd",
            "t": "abcde",
        },
        "output": "e",
    },
    {
        "input": {
            "s": "",
            "t": "y",
        },
        "output": "y",
    },
]


@pytest.mark.sol389
def test_run():
    for case in cases:
        assert (
            Solution.find_the_difference(
                s=case["input"]["s"],
                t=case["input"]["t"],
            )
            == case["output"]
        )

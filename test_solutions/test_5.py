import pytest
from solutions.sol_5 import Solution

cases = [
    {
        "input": {
            "s": "babad",
        },
        "output": "bab",
    },
    {
        "input": {
            "s": "cbbd",
        },
        "output": "bb",
    },
    {
        "input": {
            "s": "abcba",
        },
        "output": "abcba",
    },
]


@pytest.mark.sol5
def test_run():
    for case in cases:
        assert (
            Solution.longest_palindrome(
                s=case["input"]["s"],
            )
            == case["output"]
        )

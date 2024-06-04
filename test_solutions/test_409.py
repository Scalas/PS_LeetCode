import pytest
from solutions.sol_409 import Solution

cases = [
    {
        "input": {
            "s": "abccccdd",
        },
        "output": 7,
    },
    {
        "input": {
            "s": "a",
        },
        "output": 1,
    },
]


@pytest.mark.sol409
def test_run():
    for case in cases:
        assert (
            Solution.longest_palindrome(
                s=case["input"]["s"],
            )
            == case["output"]
        )

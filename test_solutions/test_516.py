import pytest
from solutions.sol_516 import Solution

cases = [
    {
        "input": {
            "s": "bbbab",
        },
        "output": 4,
    },
    {
        "input": {
            "s": "cbbd",
        },
        "output": 2,
    },
]


@pytest.mark.sol_516
def test_run():
    for case in cases:
        assert (
            Solution.longest_palindrome_subseq(
                s=case["input"]["s"],
            )
            == case["output"]
        )

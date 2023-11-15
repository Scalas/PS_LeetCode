import pytest
from solutions.sol_1930 import Solution

cases = [
    {
        "input": {
            "s": "aabca",
        },
        "output": 3,
    },
    {
        "input": {
            "s": "adc",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "bbcbaba",
        },
        "output": 4,
    },
]


@pytest.mark.sol_1930
def test_run():
    for case in cases:
        assert (
            Solution.count_palindromic_subsequence(
                s=case["input"]["s"],
            )
            == case["output"]
        )

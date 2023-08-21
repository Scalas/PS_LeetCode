import pytest
from solutions.sol_459 import Solution

cases = [
    {
        "input": {
            "s": "abab",
        },
        "output": True,
    },
    {
        "input": {
            "s": "aba",
        },
        "output": False,
    },
    {
        "input": {
            "s": "abcabcabcabc",
        },
        "output": True,
    },
]


@pytest.mark.sol_459
def test_run():
    for case in cases:
        assert (
            Solution.repeated_substring_pattern(s=case["input"]["s"]) == case["output"]
        )

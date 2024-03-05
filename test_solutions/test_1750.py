import pytest

from solutions.sol_1750 import Solution

cases = [
    {
        "input": {
            "s": "ca",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "cabaabac",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "aabccabba",
        },
        "output": 3,
    },
    {
        "input": {
            "s": "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb",
        },
        "output": 1,
    },
    {
        "input": {
            "s": "abbbbbbbbbbbbbbbbbbba",
        },
        "output": 0,
    },
]


@pytest.mark.sol1750
def test_run():
    for case in cases:
        assert (
            Solution.minimum_length(
                s=case["input"]["s"],
            )
            == case["output"]
        )

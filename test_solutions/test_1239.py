import pytest
from solutions.sol_1239 import Solution

cases = [
    {
        "input": {
            "arr": ["un", "iq", "ue"],
        },
        "output": 4,
    },
    {
        "input": {
            "arr": ["cha", "r", "act", "ers"],
        },
        "output": 6,
    },
    {
        "input": {
            "arr": ["abcdefghijklmnopqrstuvwxyz"],
        },
        "output": 26,
    },
    {
        "input": {
            "arr": ["aa", "bb", "cc"],
        },
        "output": 0,
    },
]


@pytest.mark.sol1239
def test_run():
    for case in cases:
        assert (
            Solution.max_length(
                arr=case["input"]["arr"],
            )
            == case["output"]
        )

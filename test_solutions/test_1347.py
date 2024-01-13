import pytest
from solutions.sol_1347 import Solution

cases = [
    {
        "input": {
            "s": "bab",
            "t": "aba",
        },
        "output": 1,
    },
    {
        "input": {
            "s": "leetcode",
            "t": "practice",
        },
        "output": 5,
    },
    {
        "input": {
            "s": "anagram",
            "t": "mangaar",
        },
        "output": 0,
    },
]


@pytest.mark.sol1347
def test_run():
    for case in cases:
        assert (
            Solution.min_steps(s=case["input"]["s"], t=case["input"]["t"])
            == case["output"]
        )

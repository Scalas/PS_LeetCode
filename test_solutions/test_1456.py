import pytest
from solutions.sol_1456 import Solution

cases = [
    {
        "input": {
            "s": "abciiidef",
            "k": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "s": "aeiou",
            "k": 2,
        },
        "output": 2,
    },
    {
        "input": {
            "s": "leetcode",
            "k": 3,
        },
        "output": 2,
    },
]


@pytest.mark.sol1456
def test_run():
    for case in cases:
        assert (
            Solution.max_vowels(
                s=case["input"]["s"],
                k=case["input"]["k"],
            )
            == case["output"]
        )

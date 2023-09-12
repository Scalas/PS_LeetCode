import pytest
from solutions.sol_1647 import Solution

cases = [
    {
        "input": {
            "s": "aab",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "aaabbbcc",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "ceabaacb",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "bbcebab",
        },
        "output": 2,
    },
]


@pytest.mark.sol1647
def test_run():
    for case in cases:
        assert (
            Solution.min_deletions(
                s=case["input"]["s"],
            )
            == case["output"]
        )

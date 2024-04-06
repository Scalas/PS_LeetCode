import pytest
from solutions.sol_1544 import Solution

cases = [
    {
        "input": {
            "s": "leEeetcode",
        },
        "output": "leetcode",
    },
    {
        "input": {
            "s": "abBAcC",
        },
        "output": "",
    },
    {
        "input": {
            "s": "s",
        },
        "output": "s",
    },
]


@pytest.mark.sol1544
def test_run():
    for case in cases:
        assert (
            Solution.make_good(
                s=case["input"]["s"],
            )
            == case["output"]
        )

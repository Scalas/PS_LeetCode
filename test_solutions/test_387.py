import pytest
from solutions.sol_387 import Solution

cases = [
    {
        "input": {
            "s": "leetcode",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "loveleetcode",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "aabb",
        },
        "output": -1,
    },
]


@pytest.mark.sol387
def test_run():
    for case in cases:
        assert (
            Solution.first_unique_char(
                s=case["input"]["s"],
            )
            == case["output"]
        )

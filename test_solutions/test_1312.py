import pytest
from solutions.sol_1312 import Solution

cases = [
    {
        "input": {
            "s": "zzazz",
        },
        "output": 0,
    },
    {
        "input": {
            "s": "mbadm",
        },
        "output": 2,
    },
    {
        "input": {
            "s": "leetcode",
        },
        "output": 5,
    },
]


@pytest.mark.sol1312
def test_run():
    for case in cases:
        assert (
            Solution.min_insertions(
                s=case["input"]["s"],
            )
            == case["output"]
        )

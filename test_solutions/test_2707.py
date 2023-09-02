import pytest
from solutions.sol_2707 import Solution

cases = [
    {
        "input": {
            "s": "leetscode",
            "dictionary": ["leet", "code", "leetcode"],
        },
        "output": 1,
    },
    {
        "input": {
            "s": "sayhelloworld",
            "dictionary": ["hello", "world"],
        },
        "output": 3,
    },
]


@pytest.mark.sol_2707
def test_run():
    for case in cases:
        assert (
            Solution.min_extra_char(
                s=case["input"]["s"], dictionary=case["input"]["dictionary"]
            )
            == case["output"]
        )

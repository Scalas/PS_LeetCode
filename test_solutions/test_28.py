import pytest
from solutions.sol_28 import Solution

cases = [
    {"input": {"haystack": "sadbutsad", "needle": "sad"}, "output": 0},
    {"input": {"haystack": "leetcode", "needle": "leeto"}, "output": -1},
]


@pytest.mark.sol28
def test_run():
    for case in cases:
        assert (
            Solution.str_str(
                haystack=case["input"]["haystack"], needle=case["input"]["needle"]
            )
            == case["output"]
        )

import pytest
from solutions.sol_1957 import Solution


cases = [
    {
        "input": {"s": "leeetcode"},
        "output": "leetcode",
    },
    {
        "input": {"s": "aaabaaaa"},
        "output": "aabaa",
    },
    {
        "input": {"s": "aab"},
        "output": "aab",
    },
]


@pytest.mark.sol1957
def test_run():
    for case in cases:
        assert (
            Solution.make_fancy_string(
                s=case["input"]["s"],
            )
            == case["output"]
        )

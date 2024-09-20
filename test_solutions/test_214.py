import pytest
from solutions.sol_214 import Solution


cases = [
    {
        "input": {"s": "abcabcacab"},
        "output": "bacacbacbabcabcacab",
    },
    {
        "input": {"s": "aacecaaa"},
        "output": "aaacecaaa",
    },
    {
        "input": {"s": "abcd"},
        "output": "dcbabcd",
    },
    {
        "input": {"s": "babbbabbaba"},
        "output": "ababbabbbabbaba",
    },
]


@pytest.mark.sol214
def test_run():
    for case in cases:
        assert (
            Solution.shortestPalindrome(
                s=case["input"]["s"],
            )
            == case["output"]
        )

import pytest
from solutions.sol_1684 import Solution


cases = [
    {
        "input": {"allowed": "ab", "words": ["ad", "bd", "aaab", "baa", "badab"]},
        "output": 2,
    },
    {
        "input": {"allowed": "abc", "words": ["a", "b", "c", "ab", "ac", "bc", "abc"]},
        "output": 7,
    },
    {
        "input": {
            "allowed": "cad",
            "words": ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"],
        },
        "output": 4,
    },
]


@pytest.mark.sol1684
def test_run():
    for case in cases:
        assert (
            Solution.count_consistent_strings(
                allowed=case["input"]["allowed"],
                words=case["input"]["words"],
            )
            == case["output"]
        )

import pytest
from solutions.sol_916 import Solution


cases = [
    {
        "input": {
            "words1": ["amazon", "apple", "facebook", "google", "leetcode"],
            "words2": ["e", "o"],
        },
        "output": ["facebook", "google", "leetcode"],
    },
    {
        "input": {
            "words1": ["amazon", "apple", "facebook", "google", "leetcode"],
            "words2": ["l", "e"],
        },
        "output": ["apple", "google", "leetcode"],
    },
]


@pytest.mark.sol916
def test_run():
    for case in cases:
        assert (
            Solution.word_subsets(
                words2=case["input"]["words2"],
                words1=case["input"]["words1"],
            )
            == case["output"]
        )

import pytest
from solutions.sol_139 import Solution

cases = [
    {
        "input": {
            "s": "leetcode",
            "word_dict": ["leet", "code"],
        },
        "output": True,
    },
    {
        "input": {
            "s": "applepenapple",
            "word_dict": ["apple", "pen"],
        },
        "output": True,
    },
    {
        "input": {
            "s": "catsandog",
            "word_dict": ["cats", "dog", "sand", "and", "cat"],
        },
        "output": False,
    },
]


@pytest.mark.sol139
def test_run():
    for case in cases:
        assert (
            Solution.word_break(
                s=case["input"]["s"],
                word_dict=case["input"]["word_dict"],
            )
            == case["output"]
        )

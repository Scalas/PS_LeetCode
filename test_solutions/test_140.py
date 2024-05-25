import pytest
from solutions.sol_140 import Solution

cases = [
    {
        "input": {
            "s": "catsanddog",
            "word_dict": ["cat", "cats", "and", "sand", "dog"],
        },
        "output": ["cats and dog", "cat sand dog"],
    },
    {
        "input": {
            "s": "pineapplepenapple",
            "word_dict": ["apple", "pen", "applepen", "pine", "pineapple"],
        },
        "output": [
            "pine apple pen apple",
            "pineapple pen apple",
            "pine applepen apple",
        ],
    },
    {
        "input": {
            "s": "catsandog",
            "word_dict": ["cats", "dog", "sand", "and", "cat"],
        },
        "output": [],
    },
]


@pytest.mark.sol140
def test_run():
    for case in cases:
        assert sorted(
            Solution.word_break(
                s=case["input"]["s"],
                word_dict=case["input"]["word_dict"],
            )
        ) == sorted(case["output"])

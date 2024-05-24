import pytest
from solutions.sol_1255 import Solution

cases = [
    {
        "input": {
            "words": ["dog", "cat", "dad", "good"],
            "letters": ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
            "score": [
                1,
                0,
                9,
                5,
                0,
                0,
                3,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                2,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        },
        "output": 23,
    },
    {
        "input": {
            "words": ["xxxz", "ax", "bx", "cx"],
            "letters": ["z", "a", "b", "c", "x", "x", "x"],
            "score": [
                4,
                4,
                4,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                0,
                5,
                0,
                10,
            ],
        },
        "output": 27,
    },
    {
        "input": {
            "words": ["leetcode"],
            "letters": ["l", "e", "t", "c", "o", "d"],
            "score": [
                0,
                0,
                1,
                1,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
            ],
        },
        "output": 0,
    },
]


@pytest.mark.sol1255
def test_run():
    for case in cases:
        assert (
            Solution.max_score_words(
                words=case["input"]["words"],
                letters=case["input"]["letters"],
                score=case["input"]["score"],
            )
            == case["output"]
        )

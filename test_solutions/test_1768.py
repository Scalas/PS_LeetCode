import pytest
from solutions.sol_1768 import Solution

cases = [
    {
        "input": {
            "word1": "abc",
            "word2": "pqr",
        },
        "output": "apbqcr",
    },
    {
        "input": {
            "word1": "ab",
            "word2": "pqrs",
        },
        "output": "apbqrs",
    },
    {
        "input": {
            "word1": "abcd",
            "word2": "pq",
        },
        "output": "apbqcd",
    },
]


@pytest.mark.sol1768
def test_run():
    for case in cases:
        assert (
            Solution.merge_alternately(
                word1=case["input"]["word1"],
                word2=case["input"]["word2"],
            )
            == case["output"]
        )

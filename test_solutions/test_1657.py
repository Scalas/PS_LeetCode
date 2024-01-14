import pytest
from solutions.sol_1657 import Solution

cases = [
    {
        "input": {
            "word1": "abc",
            "word2": "bca",
        },
        "output": True,
    },
    {
        "input": {
            "word1": "a",
            "word2": "aa",
        },
        "output": False,
    },
    {
        "input": {
            "word1": "cabbba",
            "word2": "abbccc",
        },
        "output": True,
    },
]


@pytest.mark.sol1657
def test_run():
    for case in cases:
        assert (
            Solution.close_strings(
                word1=case["input"]["word1"],
                word2=case["input"]["word2"],
            )
            == case["output"]
        )

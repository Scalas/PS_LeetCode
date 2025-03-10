import pytest
from solutions.sol_3306 import Solution


cases = [
    {
        "input": {"word": "aeioqq", "k": 1},
        "output": 0,
    },
    {
        "input": {"word": "aeiou", "k": 0},
        "output": 1,
    },
    {
        "input": {"word": "ieaouqqieaouqq", "k": 1},
        "output": 3,
    },
]


@pytest.mark.sol3306
def test_run():
    for case in cases:
        assert (
            Solution.count_of_substrings(
                k=case["input"]["k"],
                word=case["input"]["word"],
            )
            == case["output"]
        )

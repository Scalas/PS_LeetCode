import pytest
from solutions.sol_1915 import Solution

cases = [
    {
        "input": {
            "word": "aba",
        },
        "output": 4,
    },
    {
        "input": {
            "word": "aabb",
        },
        "output": 9,
    },
    {
        "input": {
            "word": "he",
        },
        "output": 2,
    },
    {
        "input": {
            "word": "hejaabbc",
        },
        "output": 17,
    },
]


@pytest.mark.sol1915
def test_run():
    for case in cases:
        assert (
            Solution.wonderful_substrings(
                word=case["input"]["word"],
            )
            == case["output"]
        )

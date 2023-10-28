import pytest
from solutions.sol_1220 import Solution

cases = [
    {
        "input": {
            "n": 1,
        },
        "output": 5,
    },
    {
        "input": {
            "n": 2,
        },
        "output": 10,
    },
    {
        "input": {
            "n": 5,
        },
        "output": 68,
    },
    {
        "input": {
            "n": 144,
        },
        "output": 18208803,
    },
]


@pytest.mark.sol1220
def test_run():
    for case in cases:
        assert (
            Solution.count_vowel_permutation(
                n=case["input"]["n"],
            )
            == case["output"]
        )

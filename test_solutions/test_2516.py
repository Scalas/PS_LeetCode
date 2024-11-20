import pytest
from solutions.sol_2516 import Solution


cases = [
    {
        "input": {
            "s": "aabaaaacaabc", "k": 2
        },
        "output": 8,
    },
    {
        "input": {
            "s": "a", "k": 1
        },
        "output": -1,
    },
    {
        "input": {
            "s": "bcb", "k": 0
        },
        "output": 0,
    },
    {
        "input": {
            "s": "aacbca", "k": 1
        },
        "output": 3,
    },
    {
        "input": {
            "s": "aabbccca", "k": 2
        },
        "output": 6,
    },
]


@pytest.mark.sol2516
def test_run():
    for case in cases:
        assert (
            Solution.take_characters(
                s=case["input"]["s"],
                k=case["input"]["k"],
            )
            == case["output"]
        )

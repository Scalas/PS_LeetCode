import pytest
from solutions.sol_1531 import Solution

cases = [
    {
        "input": {
            "s": "aaabcccd",
            "k": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "s": "aabbaa",
            "k": 2,
        },
        "output": 2,
    },
    {
        "input": {
            "s": "aaaaaaaaaaa",
            "k": 0,
        },
        "output": 3,
    },
]


@pytest.mark.sol1531
def test_run():
    for case in cases:
        assert (
            Solution.get_length_of_optimal_compression(
                s=case["input"]["s"],
                k=case["input"]["k"],
            )
            == case["output"]
        )

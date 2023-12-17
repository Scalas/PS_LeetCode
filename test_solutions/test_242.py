import pytest
from solutions.sol_242 import Solution

cases = [
    {
        "input": {
            "s": "anagram",
            "t": "nagaram",
        },
        "output": True,
    },
    {
        "input": {
            "s": "rat",
            "t": "car",
        },
        "output": False,
    },
]


@pytest.mark.sol242
def test_run():
    for case in cases:
        assert (
            Solution.is_anagram(
                s=case["input"]["s"],
                t=case["input"]["t"],
            )
            == case["output"]
        )

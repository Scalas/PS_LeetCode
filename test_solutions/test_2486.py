import pytest
from solutions.sol_2486 import Solution

cases = [
    {
        "input": {"s": "coaching", "t": "coding"},
        "output": 4,
    },
    {
        "input": {"s": "abcde", "t": "a"},
        "output": 0,
    },
    {
        "input": {"s": "z", "t": "abcde"},
        "output": 5,
    },
]


@pytest.mark.sol_2486
def test_run():
    for case in cases:
        assert (
            Solution.append_characters(
                s=case["input"]["s"],
                t=case["input"]["t"],
            )
            == case["output"]
        )

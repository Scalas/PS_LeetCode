import pytest
from solutions.sol_1318 import Solution

cases = [
    {
        "input": {
            "a": 2,
            "b": 6,
            "c": 5,
        },
        "output": 3,
    },
    {
        "input": {
            "a": 4,
            "b": 2,
            "c": 7,
        },
        "output": 1,
    },
    {
        "input": {
            "a": 1,
            "b": 2,
            "c": 3,
        },
        "output": 0,
    },
    {
        "input": {
            "a": 8,
            "b": 3,
            "c": 5,
        },
        "output": 3,
    },
]


@pytest.mark.sol1318
def test_run():
    for case in cases:
        assert (
            Solution.min_flips(
                a=case["input"]["a"],
                b=case["input"]["b"],
                c=case["input"]["c"],
            )
            == case["output"]
        )

import pytest
from solutions.sol_201 import Solution

cases = [
    {
        "input": {
            "left": 5,
            "right": 7,
        },
        "output": 4,
    },
    {
        "input": {
            "left": 0,
            "right": 0,
        },
        "output": 0,
    },
    {
        "input": {
            "left": 1,
            "right": 2147483647,
        },
        "output": 0,
    },
    {
        "input": {
            "left": 1,
            "right": 3,
        },
        "output": 0,
    },
]


@pytest.mark.sol201
def test_run():
    for case in cases:
        assert (
            Solution.range_bitwise_and(
                left=case["input"]["left"],
                right=case["input"]["right"],
            )
            == case["output"]
        )

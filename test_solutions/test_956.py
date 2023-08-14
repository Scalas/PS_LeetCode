import pytest
from solutions.sol_956 import Solution

cases = [
    {
        "input": {
            "rods": [1, 2, 3, 6],
        },
        "output": 6,
    },
    {
        "input": {
            "rods": [1, 2, 3, 4, 5, 6],
        },
        "output": 10,
    },
    {
        "input": {
            "rods": [1, 2],
        },
        "output": 0,
    },
    {
        "input": {
            "rods": [
                102,
                101,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
                100,
            ],
        },
        "output": 900,
    },
]


@pytest.mark.sol956
def test_run():
    for case in cases:
        assert Solution.tallest_billboard(rods=case["input"]["rods"]) == case["output"]

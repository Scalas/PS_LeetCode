import pytest
from solutions.sol_1208 import Solution

cases = [
    {
        "input": {
            "s": "abcd",
            "t": "bcdf",
            "max_cost": 3,
        },
        "output": 3,
    },
    {
        "input": {
            "s": "abcd",
            "t": "cdef",
            "max_cost": 3,
        },
        "output": 1,
    },
    {
        "input": {
            "s": "abcd",
            "t": "acde",
            "max_cost": 0,
        },
        "output": 1,
    },
    {
        "input": {
            "s": "krrgw",
            "t": "zjxss",
            "max_cost": 19,
        },
        "output": 2,
    },
]


@pytest.mark.sol1208
def test_run():
    for case in cases:
        assert (
            Solution.equal_substring(
                s=case["input"]["s"],
                t=case["input"]["t"],
                max_cost=case["input"]["max_cost"],
            )
            == case["output"]
        )

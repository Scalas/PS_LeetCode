import pytest
from solutions.sol_1269 import Solution

cases = [
    {
        "input": {
            "steps": 3,
            "arr_len": 2,
        },
        "output": 4,
    },
    {
        "input": {
            "steps": 2,
            "arr_len": 4,
        },
        "output": 2,
    },
    {
        "input": {
            "steps": 4,
            "arr_len": 2,
        },
        "output": 8,
    },
    {
        "input": {
            "steps": 27,
            "arr_len": 7,
        },
        "output": 127784505,
    },
]


@pytest.mark.sol1269
def test_run():
    for case in cases:
        assert (
            Solution.num_ways(
                steps=case["input"]["steps"],
                arr_len=case["input"]["arr_len"],
            )
            == case["output"]
        )
